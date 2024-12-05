import time

class Vehicle:
    def change_direction(left, on):
        pass
    def turn(left):
        change_direction(left,True)
        time.sleep(0.25)
        change_direction(left, False)
class TrackedVehicle(Vehicle):
    def change_direction(left, on):
        control_track(left, on)
    def control_track(left, stop):
        pass


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass
    def change_direction(left, on):
        turn_front_wheels(left, on)
        
# !the inheritance path cannot be altered. don't fuck up the method resolution order -> class Bottome(Top, Middle) ??
