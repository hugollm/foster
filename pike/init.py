import os.path
import shutil

import click


@click.command()
def init():
    create_package_file()

def create_package_file():
    if os.path.exists('package.py'):
        return click.secho('ERROR: pike refuses to overwrite existing package.py', err=True, fg='red')
    shutil.copy(source_path(), 'package.py')
    click.secho('OK: package.py', fg='green')

def source_path():
    pike_dir = os.path.dirname(__file__)
    return os.path.join(pike_dir, 'samples', 'package.py')
