import media
import fresh_tomatoes

# movie objects to be added to the list below
the_hitmans_bodyguard = media.Movie(
    "https://www.youtube.com/watch?v=F4Afusxc2SM",
    "tt1959563")

american_made = media.Movie(
    "https://www.youtube.com/watch?v=AEBIJRAkujM",
    "tt3532216")

guardians_of_the_galaxy = media.Movie(
    "https://www.youtube.com/watch?v=d96cjJhvlMA",
    "tt2015381")

# list to store movies
movies = [the_hitmans_bodyguard, american_made, guardians_of_the_galaxy]
# build webpage using fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
