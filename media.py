import urllib2
import json


class Movie():
    """Class to retrieve and store movie data."""

    apikey = "2299bccb"  # enter your OMDb API key as a string

    def __init__(self, trailer_youtube_url, imdb_id):
        self.url = "http://www.omdbapi.com/?apikey="+self.apikey+"&i="+imdb_id
        self.data = json.load(urllib2.urlopen(self.url))
        self.title = self.data['Title']
        self.poster_image_url = self.data['Poster']
        self.trailer_youtube_url = trailer_youtube_url
        self.runtime = self.data['Runtime']
        self.rated = self.data['Rated']
        self.imdb_rating = self.data['imdbRating']
