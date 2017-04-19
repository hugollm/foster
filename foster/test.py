from subprocess import call

from .command import Command
from .utils import sample_path


class Test(Command):

    def run(self, *args):
        if not args:
            self.abort('ABORT: missing PACKAGE argument')
        args = ' '.join(args)
        call(['pip install -i https://testpypi.python.org/pypi ' + args], shell=True)
