import unittest
import sys
sys.path.insert(0, '../src')
from babysittertime import BabySitterTime

class BabySitterTimeTest(unittest.TestCase):
    _clock = BabySitterTime()


if __name__ == '__main__':
    unittest.main()
