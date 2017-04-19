from importlib import import_module
import os
import shutil
from subprocess import call

from .command import Command
from .utils import copy_sample, render_sample


class Build(Command):

    def run(self):
        settings = self.get_settings_from_package_file()
        self.create_boilerplate_files(settings)
        self.remove_old_dist_directory()
        self.run_setup()
        self.remove_boilerplate_files(settings)

    def create_boilerplate_files(self, settings):
        self.create_setup_file(settings)
        self.create_manifest_file(settings)

    def get_settings_from_package_file(self):
        module = import_module('package')
        keys = [
            'name',
            'version',
            'packages',
            'files',
            'requirements',
            'scripts',
            'author',
            'author_email',
            'license',
            'url',
            'keywords',
            'description',
            'long_description',
        ]
        return {key: getattr(module, key) for key in keys}

    def create_setup_file(self, settings):
        setup = render_sample('setup.py', **settings)
        with open('setup.py', 'w') as target:
            target.write(setup)

    def create_manifest_file(self, settings):
        if not settings['files']:
            return
        with open('MANIFEST.in', 'w') as f:
            for item in settings['files']:
                if os.path.isfile(item):
                    f.write('include ' + item + '\n')
                elif os.path.isdir(item):
                    f.write('recursive-include ' + item + ' *' + '\n')

    def remove_old_dist_directory(self):
        if os.path.isdir('dist'):
            shutil.rmtree('dist')

    def run_setup(self):
        call(['python', 'setup.py', 'sdist', 'bdist_wheel', '--universal'])

    def remove_boilerplate_files(self, settings):
        os.unlink('setup.py')
        if os.path.exists('MANIFEST.in'):
            os.unlink('MANIFEST.in')
        shutil.rmtree('build')
        shutil.rmtree(settings.get('name') + '.egg-info')
