name = 'foster'
version = '0.1.0'

packages = ['foster']
files = ['foster/samples', 'LICENSE']
requirements = ['twine >= 1, < 2']
scripts = ['foster=foster.main:run']

author = 'Hugo Leonardo Leão Mota'
author_email = 'hugo.txt@gmail.com'
license = 'MIT'
url = 'https://github.com/hugollm/foster'

keywords = 'foster python package build publish'
description = 'An easy way to publish your python packages'

long_description = """
Foster is a thin wrapper around twine, making it easier to build and publish python packages.
"""
