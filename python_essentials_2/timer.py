class Timer:

    def __init__( self, hour, minutes, seconds ):

        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds


    def __str__(self):
        return f"{str(self.hour).rjust(2,'0')}:{str(self.minutes).rjust(2, '0')}:{str(self.seconds).rjust(2,'0')}"


    def next_second(self):
        self.seconds += 1
        if (self.seconds == 60):
            self.seconds = 0

            self.minutes += 1

            if self.minutes == 60:

                self.minutes = 0

                self.hour += 1 

                if self.hour == 24:

                    self.hour = 0


    def prev_second(self):
        self.seconds = (self.seconds - 1) % 60
        if (self.seconds == 59):

            self.minutes = (self.minutes -1) % 60 

            if self.minutes == 59:

                self.hour = (self.hour - 1) % 24


timer = Timer(23, 59, 59)

print(timer)

timer.next_second()

print(timer)

timer.prev_second()

print(isinstance(timer, Timer))
print(issubclass(Timer, Exception))