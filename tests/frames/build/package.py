name = 'foobar'
version = '0.0.0'

packages = ['foobar']
files = ['README.md']
requirements = ['Jinja2']
scripts = ['foo=foobar.foo:foo', 'bar=foobar.bar:bar']

author = 'John Doe'
author_email = 'john.doe@some.domain.com'
license = 'MIT'
url = 'http://some.domain.com/foo/bar'

keywords = 'foo bar'
description = "Should not fail if text contains single quotes ' like this."
long_description = 'Should not fail if text contains """ like this.'
