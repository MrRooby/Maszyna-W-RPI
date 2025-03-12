
from rpi_ws281x import *

class BinaryLine:
    def __init__(self, strip=None, start_index=0, color=Color(0, 0, 0)):
        self.strip = strip
        self.start_index = start_index
        self.segment_color = color
    
    def __to_bin(self, value):
        if not isinstance(value, (int, float)):
            value = 0
        if value < 0:
            value = 0
        elif value > 255:
            value = 255

        return [7 - i for i, bit in enumerate(format(value, '08b')) if bit == '1']

    def display_value(self, value):
        turn_on = self.__to_bin(value)

        # Clear all segments first
        for i in range(8):
            self.strip.setPixelColor(self.start_index + i, Color(0, 0, 0))
        
        for n in turn_on:
            self.strip.setPixelColor(self.start_index + n, self.segment_color)

        self.strip.show()

    def change_color(self, color):
        self.segment_color = color
