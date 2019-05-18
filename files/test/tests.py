import unittest
import sys
sys.path.insert(0, '../src')
from babysittertime import BabySitterTime

class BabySitterTimeTest(unittest.TestCase):
    _clock = BabySitterTime()

    def testStartTimeSet(self):
        for index in xrange(0, 24):
            if (index >= 0 and index <= 3) or (index >= 17 and index <=24):
                self.assertTrue(self._clock.StartTime(index))
            else:
                self.assertFalse(self._clock.StartTime(index))

    def testEndTimeSet(self):
        for index in xrange(0, 24):
            if (index >= 0 and index <= 4) or (index >= 18 and index <= 24):
                self.assertTrue(self._clock.EndTime(index))
            else:
                self.assertFalse(self._clock.EndTime(index))

    def testValidTimesSet(self):
        self.assertFalse(self._clock.StartTime(25))
        self.assertFalse(self._clock.EndTime(25))
        self.assertFalse(self._clock.StartTime(-1))
        self.assertFalse(self._clock.EndTime(-1))

    def testTimesAreValid(self):
        self.assertTrue(self._clock.CreateShift(17, 4))

    def testTimesAreInsideWorkHours(self):
        self.assertFalse(self._clock.CreateShift(16, 4))
        self.assertFalse(self._clock.CreateShift(17, 5))

    def testTimeOrder(self):
        self.assertTrue(self._clock.CreateShift(19,20))
        self.assertFalse(self._clock.CreateShift(20,19))

    def testSetFamily(self):
        self._clock.SetFamily('A')
        self.assetEqual(self._clock._shiftFamily, 'A')

if __name__ == '__main__':
    unittest.main()
