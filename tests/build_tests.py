from unittest import TestCase
import os
import shutil

from pike.build import Build


class BuildTestCase(TestCase):

    def setUp(self):
        root = os.path.join(os.path.dirname(__file__), 'frames', 'build')
        os.chdir(root)

    def tearDown(self):
        if os.path.exists('setup.py'):
            os.unlink('setup.py')
        if os.path.exists('MANIFEST.in'):
            os.unlink('MANIFEST.in')
        if os.path.exists('build'):
            shutil.rmtree('build')
        if os.path.exists('foobar.egg-info'):
            shutil.rmtree('foobar.egg-info')
        if os.path.exists('dist'):
            shutil.rmtree('dist')

    def test_build_executes_without_error(self):
        Build().run()
        self.assertTrue(os.path.isdir('dist'))

    def test_build_command_creates_build_files(self):
        Build().run()
        self.assertTrue(os.path.isfile('dist/foobar-0.0.0.tar.gz'))
        self.assertTrue(os.path.isfile('dist/foobar-0.0.0-py2.py3-none-any.whl'))

    def test_build_does_not_leave_garbage_behind(self):
        Build().run()
        self.assertFalse(os.path.isfile('setup.py'))
        self.assertFalse(os.path.isfile('MANIFEST.in'))
        self.assertFalse(os.path.isdir('foobar.egg-info'))
        self.assertFalse(os.path.isdir('build'))

    def test_create_setup_file(self):
        build = Build()
        settings = build.get_settings_from_package_file()
        build.create_setup_file(settings)
        with open('setup.py', 'r') as f:
            setup = f.read()
            self.assertIn('name = \'foobar\'', setup)
            self.assertIn('version = \'0.0.0\'', setup)
            self.assertIn('install_requires = [\'Jinja2\']', setup)
            self.assertIn('entry_points = {\'console_scripts\': [\'foo=foobar.foo:foo\', \'bar=foobar.bar:bar\']}', setup)

    def test_create_manifest_file(self):
        settings = {'files': ['README.md', 'foobar/bar']}
        Build().create_manifest_file(settings)
        with open('MANIFEST.in', 'r') as f:
            manifest = f.read()
            expected = 'include README.md\nrecursive-include foobar/bar *\n'
            self.assertEqual(manifest, expected)

    def test_manifest_is_not_created_if_theres_no_files_to_include(self):
        settings = {'files': []}
        Build().create_manifest_file(settings)
        self.assertFalse(os.path.isfile('MANIFEST.in'))

    def test_build_command_overwrites_stale_dist_directory(self):
        os.mkdir('dist')
        open('dist/foobar.stale', 'a').close()
        Build().run()
        self.assertFalse(os.path.isfile('dist/foobar.stale'))
