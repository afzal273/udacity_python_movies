__author__ = 'asyed'

import webbrowser
import urllib
import json

with open('rt_api_key.txt', 'r') as f:
    api_key = f.read()


class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_id, image, trailer_youtube):
        """initialize title, poster image, youtube trailer url and other details
           Rotten Tomatoes API has all details besides poster image and youtube url
           http://api.rottentomatoes.com/api/public/v1.0/movies/770672122.json?apikey=your_api_key
        """

        contents = urllib.urlopen(
            "http://api.rottentomatoes.com/api/public/v1.0/movies/" + str(movie_id) + ".json?apikey=" + api_key)
        data = json.loads(contents.read())
        self.title = data['title']
        self.storyline = data['synopsis']
        self.poster_image_url = image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = data['release_dates']['theater']
        self.mpaa_rating = data['mpaa_rating']
        self.year = data['year']

    def show_trailer(self):
        """Open trailer in a browser"""

        webbrowser.open(self.trailer_youtube_url)
