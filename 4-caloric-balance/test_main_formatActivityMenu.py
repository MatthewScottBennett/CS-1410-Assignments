"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import sys
if sys.version_info.major != 3:
    print('You must use Python 3.x version to run this unit test')
    sys.exit(1)

import unittest
import re

import main


class TestFormatActivityMenu(unittest.TestCase):
    def test001_formatActivityMenuExists(self):
        self.assertTrue('formatActivityMenu' in dir(main),
                        'Function "formatActivityMenu" is not defined, check your spelling')
        return

    def test002_formatMenuContainsAllActions(self):
        from main import formatActivityMenu
        actual = formatActivityMenu()
        self.assertTrue(type(actual) is list, 'formatActivityMenu did not return a list. It should return a list of strings.')
        self.assertGreaterEqual(len(actual), 5,
            'You should have at least 5 lines. 1+ for instructions, 4+ for chosen activities.')

        menu = formatActivityMenu()
        options = []
        for line in menu:
            matches = re.findall("\[([a-z0-9]+)\]", line)
            if len(matches) > 0:
                options += matches

        self.assertGreaterEqual(len(options), 4,
            "Not enough options located in your instructions. Each option should contain '[?]' where the value of ? consists of letters (a-z) and/or numbers (0-9).")


if __name__ == '__main__':
    unittest.main()
