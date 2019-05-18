import unittest
import sys
sys.path.insert(0, '../src')
from babysittertime import BabySitterTime

class BabySitterTimeTest(unittest.TestCase):
    _clock = BabySitterTime()

    def testStartTimeSet(self):
        self.assertTrue(self._clock.setStartTime())

    def testEndTimeSet(self):
        self.assertTrue(self._clock.setStartTime())


if __name__ == '__main__':
    unittest.main()
