class BabySitterTimeTest:
    _clock = None
    def __init__(self):
        execfile("../src/babysittertime")
        self._clock = BabySitterTime()
