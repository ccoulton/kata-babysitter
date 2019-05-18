class BabySitterTime:
    _startTime = None
    _endTime = None
    def __init__(self):
        self._startTime = 0
        self._endTime = 0

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
        else:
            return False

    def StartTime(self, inputTime):
        if self._checkTime(17, 3, inputTime):
            self._startTime = inputTime
            return True
        else:
            return False

    def EndTime(self, inputTime):
        if self._checkTime(18, 4, inputTime):
            self._endTime = inputTime
            return True
        else:
            return False

    def CreateShift(self, start, end):
        if self.StartTime(start) and self.EndTime(end):
            if start <4:
                start += 24
            if end < 5:
                end += 24
            return start < end
        return False
    #alternitvly you could throw an exception when values are not correct
    #allowing for input to be put in a try block in application.

    def ValidShift(self):
        start = 0
        end = 0
        if self._startTime <4:
            start = self._startTime + 24
        if self._endTime <5:
            end = self._endTime +24
        return start < end

def main():
    shifts = {}
    shifts[0] = BabySitterTime()
    print("Times to be inserted in 24 hour clock times, rounded to nearest hour")
    print("ignoring mintues.")
    while not shifts[0].ValidShift():
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
