from subprocess import call
import click
from .utils import sample_path


@click.command()
@click.argument('env', nargs=1)
def register(env):
    if env not in ('staging', 'production'):
        raise click.ClickException('Invalid env. Options are: staging, production')
    call(['twine register -r dist/* --config-file ' + sample_path('pypirc') + ' -r ' + env], shell=True)
