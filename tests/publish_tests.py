from unittest import TestCase
import os
import shutil

from foster.build import Build
from foster.publish import Publish


class RegisterTestCase(TestCase):

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

    def test_publish_does_not_run_if_no_env_is_specified(self):
        Build().run()
        with self.assertRaises(SystemExit):
            Publish().run()
