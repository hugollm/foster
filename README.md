# Foster

Foster care for your python projects. This tool is a simple way to build and publish your packages to PyPI, making them available for a `pip install`.


## Quickstart

Install foster:

    pip install foster

Init your package settings:

    foster init

This will create a `package.py` file in your current directory (this should be the root of your project).
This is the only file you need to commit to your version control (git).

Edit the file with your package information. Example:

```python
name = 'myproject'
version = '0.0.0'

packages = ['myproject', 'myproject.subpackage']
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
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""
```

In the above example, the package will:

* Include the python packages `myproject` and `myproject.subpackage`
* Include all the files in the `myproject/files` directory (recursively) and the `LICENSE` file
* Add `Jinja2` (version 2.x.x) as a requirement (it's probably not a good idea to pinpoint the version, but you can)
* Add the console script `myp`, making it execute the `run` callable in the `myproject.command` file

If you're not using some of the fields, like `files` or `scripts` for instance, just leave them empty (don't delete them).

Next, build your package (this will create a `dist` directory):

    foster build

Register your new package in the PyPI test environment:

    foster register staging

Change `staging` for `production` when you're ready for the real deal. The `register` command just need to be called the first time (to "claim" the project name).

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
