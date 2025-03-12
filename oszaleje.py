from rpi_ws281x import *

class Oszaleje:
    def __init__(self, strip=None, start_index=0, color=Color(0, 0, 0)):
        self.strip = strip
        self.start_index = start_index
        self.segment_color = color


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


    def __display_0(self, number):
        # Dictionary defining which segments to light for each number
        segments = {
            0: [1, 3, 92, 12, 14, 67],
            1: [1, 3],
            2: [67, 14, 73, 3, 92],
            3: [67, 14, 73, 12, 92],
            4: [1, 14, 73, 12],
            5: [67, 1, 73, 12, 92],
            6: [67, 14, 73, 12, 3, 92],
            7: [67, 14, 12, 92],
            8: [67, 1, 14, 73, 12, 3, 92],
            9: [67, 1, 14, 73, 12, 92],
        }

        # Clear all segments first
        for i in range(7):
            self.strip.setPixelColor(self.start_index + i, Color(0, 0, 0))

        # Set the active segments for the number
        if 0 <= number <= 9:
            for segment in segments[number]:
                self.strip.setPixelColor(self.start_index + segment, self.segment_color)

        # Note: We don't call strip.show() here as it should be called after all segments are updated

    def __display_1(self, number):
        # Dictionary defining which segments to light for each number
        segments = {
            0: [1, 3, 92, 12, 14, 67],
            1: [1, 3],
            2: [67, 14, 73, 3, 92],
            3: [67, 14, 73, 12, 92],
            4: [1, 14, 73, 12],
            5: [67, 1, 73, 12, 92],
            6: [67, 14, 73, 12, 3, 92],
            7: [67, 14, 12, 92],
            8: [67, 1, 14, 73, 12, 3, 92],
            9: [67, 1, 14, 73, 12, 92],
        }

        # Clear all segments first
        for i in range(7):
            self.strip.setPixelColor(self.start_index + i, Color(0, 0, 0))

        # Set the active segments for the number
        if 0 <= number <= 9:
            for segment in segments[number]:
                self.strip.setPixelColor(self.start_index + segment, self.segment_color)

        # Note: We don't call strip.show() here as it should be called after all segments are updated

    def __display_2(self, number):
        # Dictionary defining which segments to light for each number
        segments = {
            0: [1, 3, 92, 12, 14, 67],
            1: [1, 3],
            2: [67, 14, 73, 3, 92],
            3: [67, 14, 73, 12, 92],
            4: [1, 14, 73, 12],
            5: [67, 1, 73, 12, 92],
            6: [67, 14, 73, 12, 3, 92],
            7: [67, 14, 12, 92],
            8: [67, 1, 14, 73, 12, 3, 92],
            9: [67, 1, 14, 73, 12, 92],
        }

        # Clear all segments first
        for i in range(7):
            self.strip.setPixelColor(self.start_index + i, Color(0, 0, 0))

        # Set the active segments for the number
        if 0 <= number <= 9:
            for segment in segments[number]:
                self.strip.setPixelColor(self.start_index + segment, self.segment_color)

        # Note: We don't call strip.show() here as it should be called after all segments are updated

    def change_color(self, color):
        self.segment_color = color
