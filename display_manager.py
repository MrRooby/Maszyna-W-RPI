from rpi_ws281x import *
from bus_line import BusLine
from signal_line import SignalLine
from three_segment_display import ThreeSegmentDisplay
from pao_display_line import PaODisplayLine
from constants import *

class DisplayManager:
    def __init__(self, led_count_left=0, led_count_right=0, brightness=0):
        
        # LED strip configuration

        # To avoid trouble don't mess with the PIN selection
        # Those pins for sure support PWM with assigned channels
        LED_PIN_LEFT = 19       # Left side LEDs
        LED_PIN_RIGHT = 18      # Right side LEDs
        LED_FREQ_HZ = 800000
        LED_DMA = 10
        LED_INVERT = False
        LED_CHANNEL_LEFT  = 1   # Has to be that way
        LED_CHANNEL_RIGHT = 0   # or not worky 

        print(led_count_right)

        self.brightness = brightness

        self.strip_left = Adafruit_NeoPixel(
                led_count_left, 
                LED_PIN_LEFT, 
                LED_FREQ_HZ, 
                LED_DMA,
                LED_INVERT, 
                self.brightness, 
                LED_CHANNEL_LEFT)

        self.strip_right = Adafruit_NeoPixel(
                led_count_right, 
                LED_PIN_RIGHT, 
                LED_FREQ_HZ, 
                LED_DMA,
                LED_INVERT, 
                self.brightness, 
                LED_CHANNEL_RIGHT)
        
        self.strip_right.begin()
        self.strip_left.begin()
        
        #DLA TESTÓW NALEŻY POŁĄCZYĆ PIN 18
#        self.__init_left_strip()
        self.__init_right_strip()


#    def __init_left_strip(self):
#        self.busA  = BusLine(             self.strip_left, 0 , 64 , RED)
#        self.icc   = SignalLine(          self.strip_left, start_index= , length= , PORTAL_BLUE)
#        self.wec   = SignalLine(          self.strip_left, start_index= , length= , PORTAL_BLUE)
#        self.wyc   = SignalLine(          self.strip_left, start_index= , length= , PORTAL_BLUE)
#        self.c     = ThreeSegmentDisplay( self.strip_left, start_index= ,           PORTAL_ORANGE) 
#        self.wyad  = SignalLine(          self.strip_left, start_index= , length= , PORTAL_BLUE)
#        self.i     = ThreeSegmentDisplay( self.strip_left, start_index= ,           PORTAL_ORANGE)
#        self.wei   = SignalLine(          self.strip_left, start_index= , length= , PORTAL_BLUE)
#        self.weja  = SignalLine(          self.strip_left, start_index= , length= , PORTAL_BLUE)
#        self.przep = SignalLine(          self.strip_left, start_index= , length= , PORTAL_BLUE)
#        self.dak   = SignalLine(          self.strip_left, start_index= , length= , PORTAL_BLUE)
#        self.iak   = SignalLine(          self.strip_left, start_index= , length= , PORTAL_BLUE)
#        self.weak  = SignalLine(          self.strip_left, start_index= , length= , PORTAL_BLUE)
#        self.acc   = ThreeSegmentDisplay( self.strip_left, start_index= ,           PORTAL_ORANGE)


    def __init_right_strip(self):
#        self.wea   = SignalLine(          self.strip_right, start_index=0 , length=40 , PORTAL_BLUE)
        self.a     = ThreeSegmentDisplay( self.strip_right, start_index=0 , color=PORTAL_ORANGE)
#        self.PaO_1 = PaODisplayLine(      self.strip_right, start_index= ,           PORTAL_ORANGE)
#        self.PaO_2 = PaODisplayLine(      self.strip_right, start_index= ,           PORTAL_ORANGE)
#         self.czyt  = SignalLine(          self.strip_right, start_index=0 , length=5 , PORTAL_BLUE)
#        self.PaO_3 = PaODisplayLine(      self.strip_right, start_index= ,           PORTAL_ORANGE)
#        self.pisz  = SignalLine(          self.strip_right, start_index= , length= , PORTAL_BLUE)
#        self.PaO_4 = PaODisplayLine(      self.strip_right, start_index= ,           PORTAL_ORANGE)
#        self.wyak  = SignalLine(          self.strip_right, start_index= , length= , PORTAL_BLUE)
#        self.s     = ThreeSegmentDisplay( self.strip_right, start_index= ,           PORTAL_ORANGE)
#        self.wes   = SignalLine(          self.strip_right, start_index= , length= , PORTAL_BLUE)
#        self.wys   = SignalLine(          self.strip_right, start_index= , length= , PORTAL_BLUE)
#        self.busS  = BusLine(             self.strip_right, start_index= , length= , RED)


    def set_brightness(self, brightness):
        if 0 <= brightness <= 255:
            self.brightness = brightness
            self.strip_left.setBrightness(self.brightness)
            self.strip_right.setBrightness(self.brightness)
        
            self.strip_right.show()
            self.strip_left.show()
        else:
            print("Brightness value must be between 0 and 255!")


    def clear_display(self):
        for i in range(self.strip_right.numPixels()):
            self.strip_right.setPixelColor(i, Color(0, 0, 0))

        for i in range(self.strip_left.numPixels()):
            self.strip_left.setPixelColor(i, Color(0, 0, 0))

        self.strip_right.show()
        self.strip_left.show()
