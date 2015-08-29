__author__ = 'asyed'

import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, title, storyline, image, trailer_youtube):
        """initialize title, storyline, poster image and youtube trailer url"""

        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open trailer in a browser"""

        webbrowser.open(self.trailer_youtube_url)
