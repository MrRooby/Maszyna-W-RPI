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
        self.acc = [
            Segment(self.strip, 0, Color(255, 0, 0)),    # Red color
            Segment(self.strip, 7, Color(255, 0, 0)),
            Segment(self.strip, 14, Color(255, 0, 0))
        ]


    def update_acc_display(self, value):
        if value < 0:
            value = 0
        elif value > 999:
            value = 999

        # Split number into digits
        hundreds = (value // 100) % 10
        tens = (value // 10) % 10
        ones = value % 10

        # Update each segment
        self.acc[0].display_number(hundreds)
        self.acc[1].display_number(tens)
        self.acc[2].display_number(ones)

        # Update the strip
        self.strip.show()


    def clear_display(self):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(0, 0, 0))
        self.strip.show()
