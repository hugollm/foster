from importlib import import_module
import os
import shutil
from subprocess import call

import click

from .utils import copy_sample, render_sample


@click.command()
def build():
    settings = get_settings_from_package_file()
    create_boilerplate_files(settings)
    remove_old_dist_directory()
    run_setup()
    remove_boilerplate_files(settings)

def create_boilerplate_files(settings):
    create_setup_file(settings)
    create_manifest_file(settings)

def get_settings_from_package_file():
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

def create_setup_file(settings):
    pike_dir = os.path.dirname(__file__)
    setup = render_sample('setup.py', **settings)
    with open('setup.py', 'w') as target:
        target.write(setup)

def create_manifest_file(settings):
    if not settings['files']:
        return
    with open('MANIFEST.in', 'w') as f:
        for item in settings['files']:
            if os.path.isfile(item):
                f.write('include ' + item + '\n')
            elif os.path.isdir(item):
                f.write('recursive-include ' + item + ' *' + '\n')

def remove_old_dist_directory():
    if os.path.isdir('dist'):
        shutil.rmtree('dist')

def run_setup():
    call(['python', 'setup.py', 'sdist', 'bdist_wheel', '--universal'])

def remove_boilerplate_files(settings):
    os.unlink('setup.py')
    if os.path.exists('MANIFEST.in'):
        os.unlink('MANIFEST.in')
    shutil.rmtree('build')
    shutil.rmtree(settings.get('name') + '.egg-info')
