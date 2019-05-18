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

    def testValidTimesSet(self):
        self.assertFalse(self._clock.StartTime(25))
        self.assertFalse(self._clock.EndTime(25))

    def testTimesAreValid(self):
        self.assertTrue(self._clock.CreateShift(17, 4))

    def testTimesAreNotValid(self):
        self.assertFalse(self._clock.CreateShift(16, 4))
        self.assertFalse(self._clock.CreateShift(17, 5))

if __name__ == '__main__':
    unittest.main()
