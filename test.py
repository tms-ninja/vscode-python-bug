import unittest
import testissue

class Test_f(unittest.TestCase):
    def test(self):
        """Simple test"""
        self.assertEqual(1, testissue.f())
