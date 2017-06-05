import unittest
from .. import utils

class Test_utils(unittest.TestCase):

        def test_bytes_to_word_positive(self):
            self.assertEqual(utils.bytes_to_word(0x01, 0x23), 291)

        def test_bytes_to_word_negative(self):
            self.assertEqual(utils.bytes_to_word(0xab, 0xcd), -21555)

