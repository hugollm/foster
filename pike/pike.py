import click
from .init import init


@click.group()
def pike():
    pass


pike.add_command(init)


if __name__ == '__main__':
    pike()
