import os.path

from .command import Command
from .utils import copy_sample


class Init(Command):

    def run(self):
        if os.path.exists('package.py'):
            self.abort('ABORT: will not overwrite existing package.py')
        copy_sample('package.py', 'package.py')
        self.echo('OK: package.py')
