from rpi_ws281x import *
from segment import Segment

class ThreeSegmentDisplay:
    def __init__(self, strip, start_index, color):
        self.strip = strip
        self.color = color
        self.disp = self.__init_small_display(strip, start_index, color)

    def __init_small_display(self, strip, start_index, color):
        return [
            Segment(strip, start_index, color),
            Segment(strip, start_index + 7, color),
            Segment(strip, start_index + 14, color)
        ]

    def display_value(self, value):
        try:
            value = int(value)
        except ValueError:
            print("Invalid value: must be na integer")
            return

        if value < 0:
            value = 0
        elif value > 999:
            value = 999

        # Split number into digits
        hundreds = (value // 100) % 10
        tens = (value // 10) % 10
        ones = value % 10

        # Update each segment
        self.disp[0].display_number(hundreds)
        self.disp[1].display_number(tens)
        self.disp[2].display_number(ones)

        # Update the strip
        self.strip.show()

    def change_color(self, color):
        self.color = color
        for i in disp:
            disp[i].change_color(color)
