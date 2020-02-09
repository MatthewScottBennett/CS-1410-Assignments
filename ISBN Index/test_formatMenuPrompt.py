"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import isbn_index

class test_formatMenuPrompt( unittest.TestCase ):
    
    def setUp(self):
        return

    def tearDown(self):
        return
    
    def test001_formatMenuPromptExists(self):
        self.assertTrue('formatMenuPrompt' in dir( isbn_index ),
                        'Function "formatMenuPrompt" is not defined, check your spelling')
        return
    
    def test002_formatMenuPromptReturnsCorrectString(self):
        expected = "Enter an option: "
        actual = isbn_index.formatMenuPrompt( )
        self.assertEqual( actual, expected )
        return


if __name__ == '__main__':
    unittest.main()