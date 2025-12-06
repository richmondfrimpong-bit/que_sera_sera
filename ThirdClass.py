class Time:
    def __init__(self, hour=0, minute=0, seconds=0):
        self.hour = hour
        self.minute = minute
        self.seconds = seconds
        print(f'The time is {hour}:{minute}:{seconds}')
