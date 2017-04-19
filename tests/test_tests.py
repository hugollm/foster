from unittest import TestCase
import os
import shutil

from foster.build import Build
from foster.test import Test


class TestTestCase(TestCase):

    def setUp(self):
        root = os.path.join(os.path.dirname(__file__), 'frames', 'init')
        os.chdir(root)

    def test_test_command_does_not_run_if_package_is_not_specified(self):
        with self.assertRaises(SystemExit):
            Test().run()
