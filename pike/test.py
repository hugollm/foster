from subprocess import call

from .command import Command
from .utils import sample_path


class Test(Command):

    def run(self, package=None):
        if not package:
            self.abort('ABORT: missing PACKAGE argument')
        call(['pip install -i https://testpypi.python.org/pypi ' + package], shell=True)
