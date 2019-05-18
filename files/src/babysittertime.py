'''
- Family A pays $15 per hour before 11pm, and $20 per hour the rest of the night
- Family B pays $12 per hour before 10pm, $8 between 10 and 12, and $16 the rest of the night
- Family C pays $21 per hour before 9pm, then $15 the rest of the night
'''
#fam,from 5-6,  6-7,  7-8,   8-9,   9-10,  10-11, 11-12, 12-1,  1-2, 2-3,  3-4
_famA = {17:15, 18:15, 19:15, 20:15, 21:15, 22:15, 23:20, 0:20, 1:20, 2:20, 3:20}
_famB = {17:12, 18:12, 19:12, 20:12, 21:12, 22:8,  23:8,  0:16, 1:16, 2:16, 3:16}
_famC = {17:21, 18:21, 19:21, 20:21, 21:15, 22:15, 23:15, 0:15, 1:15, 2:15, 3:15}
_famDict = {'A':_famA, 'B':_famB, 'C':_famC}

class BabySitterTime:
    _shiftFamily = ''
    _startTime = None
    _endTime = None
    def __init__(self):
        self._startTime = 0
        self._endTime = 0

    def SetFamily(self, fam):
        if fam not in _famDict.keys():
            return
        self._shiftFamily = fam

    @property
    def StartTime(self):
        return self._startTime

    @property
    def EndTime(self):
        return self._endTime

    def _checkTime(self, startRange, endRange, input):
        if input >= startRange and input <= 24:
            return True
        elif input >= 0 and input <= endRange:
            return True
        #else
        return False

    def StartTime(self, inputTime):
        if self._checkTime(17, 3, inputTime):
            self._startTime = inputTime
            return True
        #else
        return False

    def EndTime(self, inputTime):
        if self._checkTime(18, 4, inputTime):
            self._endTime = inputTime
            return True
        #else
        return False

    def CreateShift(self, start, end):
        if not self.StartTime(start) or not self.EndTime(end):
            return False
        return self.ValidShift()
    #alternitvly you could throw an exception when values are not correct
    #allowing for input to be put in a try block in application.

    def ValidShift(self):
        start = self._startTime
        end = self._endTime
        if start < 4:
            start += 24
        if end < 5:
            end += 24
        return start < end

def main():
    shifts = {}
    numOfShifts = -1
    while numOfShifts < 0:
        try:
            numOfShifts = int(input("Please enter a whole number of shifts you wish to calcluate: "))
        except NameError:
            print("That is not a valid positive whole number")
            numOfShifts = -1
    for index in xrange(0, numOfShifts):
        shifts[index] = BabySitterTime()
    print("Times to be inserted in 24 hour clock times, rounded to nearest hour")
    print("ignoring mintues. i.e. 5pm is 17, 11pm is 23, and 3am is 3")
    for shift in shifts.values():
        while not shift.ValidShift():
            try:
                temp_start = int(input("Please enter your start time: "))
                temp_end = int(input("Please enter your end time: "))
                shifts[0].CreateShift(temp_start, temp_end)
            except NameError:
                print("A value you entered was not a whole number")
            except:
                print("Something went wrong please report this to:")
                print("https://github.com/ccoulton/kata-babysitter")
        print("Thank You for your input")

if __name__ == '__main__':
    main()
