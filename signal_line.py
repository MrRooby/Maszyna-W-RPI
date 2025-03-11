from rpi_ws281x import *

class SignalLine:
    def __init__(self, strip=None, start_index=0, length=0, color=Color(0, 0, 0)):
        self.strip = strip
        self.start_index = start_index
        self.color = color
        self.length = length
        print(self.strip, start_index, color, length)

    def turn_on_line(self, choice):
        if not choice:
            for i in range(self.start_index, self.length):
                self.strip.setPixelColor(i, Color(0, 0, 0))
        elif choice:
            print("line turned on")
            for i in range(self.start_index, self.length):
                self.strip.setPixelColor(i, self.color)
        self.strip.show()
    
    def change_color(self, color):
        self.color = color
