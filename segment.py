from rpi_ws281x import *

class Segment:
    def __init__(self, strip=None, start_index=0, color=Color(0, 0, 0)):
        self.strip = strip
        self.start_index = start_index
        self.segment_color = color

    def display_number(self, number):
        # Dictionary defining which segments to light for each number
        segments = {
            0: [1, 2, 3, 4, 5, 6],
            1: [1, 6],
            2: [0, 1, 2, 4, 5],
            3: [0, 1, 2, 5, 6],
            4: [0, 1, 3, 6],
            5: [0, 2, 3, 5, 6],
            6: [0, 2, 3, 4, 5, 6],
            7: [1, 2, 6],
            8: [0, 1, 2, 3, 4, 5, 6],
            9: [0, 1, 2, 3, 5, 6]
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
