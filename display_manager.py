from rpi_ws281x import *
from segment import Segment

class DisplayManager:
    def __init__(self, led_count=60, brightness=50):
        # LED strip configuration
        LED_PIN = 18      # GPIO pin connected to the pixels
        LED_FREQ_HZ = 800000
        LED_DMA = 10
        LED_BRIGHTNESS = brightness
        LED_INVERT = False
        LED_CHANNEL = 0

        self.strip = Adafruit_NeoPixel(led_count, LED_PIN, LED_FREQ_HZ, LED_DMA, 
                                     LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        self.strip.begin()

        # Initialize segments
        self.acc = self.__init_small_display(0, Color(255, 0, 0))
        # self.s   = self.__init_small_display('''starting index''', Color(255, 0, 0))
        # self.a   = self.__init_small_display('''starting index''', Color(255, 0, 0))
        # self.c   = self.__init_small_display('''starting index''', Color(255, 0, 0))
        # self.i   = self.__init_small_display('''starting index''', Color(255, 0, 0))


    def __init_small_display(self, start_index, color):
        return [
            Segment(self.strip, start_index, color),
            Segment(self.strip, start_index + 7, color),
            Segment(self.strip, start_index + 14, color)
        ]


    def __select_display(self, name: str):
        if name == "acc":
            return self.acc
        elif name == "s":
            return self.s
        elif name == "a":
            return self.a
        elif name == "c":
            return self.c
        elif name == "i":
            return self.i
        else:
            print("Input error")
            return


    def update_small_display(self, name: str, value):
        disp = self.__select_display(name)        

        if value < 0:
            value = 0
        elif value > 999:
            value = 999

        # Split number into digits
        hundreds = (value // 100) % 10
        tens = (value // 10) % 10
        ones = value % 10

        # Update each segment
        disp[0].display_number(hundreds)
        disp[1].display_number(tens)
        disp[2].display_number(ones)

        # Update the strip
        self.strip.show()


    def update_stack_display(self):
        #TODO
        self.strip.show()


    def clear_display(self):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0, 0, 0))
        self.strip.show()
