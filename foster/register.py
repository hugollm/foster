from subprocess import call

from .command import Command
from .utils import sample_path


class Register(Command):

    def run(self, env=None):
        if env not in ('staging', 'production'):
            self.abort('ABORT: invalid ENV. Options are: staging, production')
        call(['twine register -r dist/* --config-file ' + sample_path('pypirc') + ' -r ' + env], shell=True)
