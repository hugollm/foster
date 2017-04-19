import os
from unittest import TestCase
from unittest.mock import Mock

from pike.main import Main


class MainTestCase(TestCase):

    def setUp(self):
        root = os.path.join(os.path.dirname(__file__), 'frames', 'init')
        self.target = os.path.join(root, 'package.py')
        os.chdir(root)

    def tearDown(self):
        if os.path.isfile(self.target):
            os.unlink(self.target)

    def test_main_command_can_be_called_without_arguments(self):
        Main().run(['script'])

    def test_init_can_be_called_through_the_main_command(self):
        Main().run(['script', 'init'])
        self.assertTrue(os.path.isfile('package.py'))

    def test_main_shows_help_if_called_without_the_command_argument(self):
        command = Main()
        command._show_help = Mock()
        command.run(['script'])
        command._show_help.assert_called_once_with()
