import unittest
from hangman import *

class test_hangman(unittest.TestCase):
    def test_word_with_blanks(self):
        guessed_letters = "abc"
        output = print_word_with_blanks("gsp", "gossip")
        self.assertEqual(output, "g-ss-p")

if __name__ == '__main__':
    unittest.main()
