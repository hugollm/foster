import sys

import click

from .init import init
from .build import build
from .register import register


@click.group()
def pike():
    include_current_directory_in_path()

def include_current_directory_in_path():
    if '' not in sys.path:
        sys.path.append('')


pike.add_command(init)
pike.add_command(build)
pike.add_command(register)


if __name__ == '__main__':
    pike()
