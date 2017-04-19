import sys

from .command import Command
from .init import Init
from .build import Build
from .register import Register
from .publish import Publish
from .test import Test


class Main(Command):

    commands = {
        'init': Init,
        'build': Build,
        'register': Register,
        'publish': Publish,
        'test': Test,
    }

    def run(self, args=None):
        self._ensure_current_directory_is_on_path()
        print('')
        if args is None:
            args = sys.argv[:]
        args.pop(0)
        command_key = args.pop(0) if args else None
        if command_key:
            self._run_command(command_key, args)
        else:
            self._show_help()
        print('')

    def _ensure_current_directory_is_on_path(self):
        if '' not in sys.path:
            sys.path.append('')

    def _show_help(self):
        self.echo('Commands:')
        self.echo('')
        self.echo('init                Create a package.py file in your current directory')
        self.echo('build               Reads the package.py file and builds the package')
        self.echo('register ENV        Register the built package with PyPI (staging or production)')
        self.echo('publish ENV         Uploads the built package to PyPI (staging or production)')
        self.echo('test PACKAGE        Installs the specified PACKAGE from the staging server (with pip)')

    def _run_command(self, command_key, args):
        command_class = self.commands.get(command_key)
        if not command_class:
            self.abort('ABORT: Unknown command "' + command_key + '"')
        command = command_class()
        command.run(*args)


def run():
    Main().run()


if __name__ == '__main__':
    run()
