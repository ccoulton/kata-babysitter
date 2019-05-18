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
