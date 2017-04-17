from setuptools import setup

long_description = """$long_description"""

setup(
    name = '$name',
    version = '$version',

    packages = $packages,
    include_package_data = True,

    install_requires = $requirements,
    entry_points = {'console_scripts': $scripts},

    author = '$author',
    author_email = '$author_email',
    license = '$license',
    url = '$url',

    keywords = '$keywords',
    description = '$description',

    long_description = long_description,
)
