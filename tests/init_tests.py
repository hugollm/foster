import os
from unittest import TestCase
from click import ClickException
from pike.init import create_package_file


class InitTestCase(TestCase):

    def setUp(self):
        root = os.path.join(os.path.dirname(__file__), 'frames', 'init')
        self.target = os.path.join(root, 'package.py')
        os.chdir(root)

    def tearDown(self):
        if os.path.isfile(self.target):
            os.unlink(self.target)

    def test_create_package_file(self):
        create_package_file()
        self.assertTrue(os.path.isfile(self.target))
        with open(self.target, 'rb') as f:
            self.assertTrue(f.read())

    def test_create_package_dont_overwrite_existing_file(self):
        open(self.target, 'a').close()
        with self.assertRaises(ClickException):
            create_package_file()
        with open(self.target, 'rb') as f:
            self.assertEqual(f.read(), b'')
