import unittest
import sys
sys.path.insert(0, '../src')
from babysittertime import BabySitterTime

class BabySitterTimeTest(unittest.TestCase):
    _clock = BabySitterTime()

    def testStartTimeSet(self):
        self.assertTrue(self._clock.StartTime(17))
        self.assertFalse(self._clock.StartTime(16))

    def testEndTimeSet(self):
        self.assertTrue(self._clock.EndTime(4))
        self.assertFalse(self._clock.EndTime(5))


if __name__ == '__main__':
    unittest.main()
