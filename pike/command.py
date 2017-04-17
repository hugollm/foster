import sys


class Command(object):

    def echo(self, text):
        print('  ' + text)

    def abort(self, message=None):
        if message is not None:
            self.echo(message)
        print('')
        sys.exit(1)
