import time
from rpi_ws281x import *

class MainLine:
    def __init__(self, strip=None, start_index=0, length=74 ,color=Color(0, 0, 0)):
        self.strip = strip
        self.start_index = start_index
        self.color = color
        self.length = length

    def data_flow(self, from_index=None, to_index=None, choice=False):
        if from_index is None:
            from_index = self.start_index
        if to_index is None:
            to_index = self.length
        
        while choice:
            for i in range(from_index, to_index + 1):
                self.strip.setPixelColor(i, self.color)
                self.strip.setPixelColor(i + 1, self.color)
                self.strip.setPixelColor(i + 2, self.color)
                self.strip.show()
                time.sleep(50 / 1000.0)
                self.strip.setPixelColor(i, Color(0, 0, 0))
                self.strip.show()
    
    def change_color(self, color):
        self.color = color
