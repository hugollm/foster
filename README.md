# Foster

Foster is a thin wrapper around setuptools and twine, making it easier to build and publish
python packages.


## Quick start

Install foster:

    pip install foster

Init your package settings:

    foster init

This will create a `package.py` file in your current directory (this should be the root of your project). Edit the file with your package information. Example:

```python
name = 'myproject'
version = '0.0.0'

packages = ['myproject']
files = ['myproject/files', 'LICENSE']
requirements = ['Jinja2 >= 2, < 3']
scripts = ['myp=myproject.command:run']

author = 'John Doe
author_email = 'john.doe@gmail.com'
license = 'MIT'
url = 'https://github.com/...'

keywords = 'myproject awesome python'
description = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit'

long_description = """
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
```

If you're not using some of the fields, like `files` or `scripts` for instance, just leave them empty (don't delete them).

Next, build your package dist:

    foster build

Register your new package in the PyPI test environment:

    foster register staging

Change `staging` for `production` when you're ready for the real deal. The `register` command just need to be called the first time.

Finally, publish your package to the PyPI test environment:

    foster publish staging

Again, change `staging` for `production` when you're done testing.

Packages uploaded to the PyPI's test environment can be tested with:

    pip install -i https://testpypi.python.org/pypi myproject

Or, more easily:

    foster test myproject

If your package has dependencies, you'll have to install them from the standard repository first:

    pip install Jinja2
    foster test myproject
