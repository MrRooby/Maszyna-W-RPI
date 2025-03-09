from rpi_ws281x import *
from two_segment_display import TwoSegmentDisplay
from three_segment_display import ThreeSegmentDisplay

class PaODisplayLine:
    def __init__(self, strip, start_index, color):
        self.strip = strip
        self.color = color
        
        self.addr = TwoSegmentDisplay(self.strip, start_index, self.color) 
        self.val  = ThreeSegmentDisplay(self.strip, start_index + 14, self.color)
        self.arg  = TwoSegmentDisplay(self.strip, start_index + 35, self.color)


    def display_line(self, addr, val, arg):
        self.addr.display_value(addr)
        self.val.display_value(val)
        self.arg.display_value(arg)
        

