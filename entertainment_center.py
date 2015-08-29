__author__ = 'asyed'

import media
import fresh_tomatoes

# Making movie objects from the media module

paddington = media.Movie("Paddington",
                         "A bear living with humans",
                         "https://upload.wikimedia.org/wikipedia/en/0/06/PaddingtonPOSTER.jpg",
                         "https://www.youtube.com/watch?v=qFuzMlfZGWM")

mad_max_fury = media.Movie("Mad Max Fury Road",
                           "A post apocalyptic movie",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg/220px-Max_Mad_Fury_Road_Newest_Poster.jpg",
                           "https://www.youtube.com/watch?v=hEJnMQG9ev8")

inside_out = media.Movie("Inside Out",
                         "A major emotion picture!",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/0/0a/Inside_Out_%282015_film%29_poster.jpg/220px-Inside_Out_%282015_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=seMwpP0yeu4")

interstellar = media.Movie("Interstellar",
                           "An intergalactic travel movie",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Interstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw")

big_hero_6 = media.Movie("Big Hero 6",
                         "A robotic doctor!",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/Big_Hero_6_%28film%29_poster.jpg/220px-Big_Hero_6_%28film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=z3biFxZIJOQ")

peabody_sherman = media.Movie("Mr. Peabody & Sherman",
                              "The smartest dog in the world adopts a boy",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/5/58/Mr_Peabody_%26_Sherman_Poster.JPG/220px-Mr_Peabody_%26_Sherman_Poster.JPG",
                              "https://www.youtube.com/watch?v=hy6oD7BZw50")

movies = [paddington, mad_max_fury, inside_out,
          interstellar, big_hero_6, peabody_sherman]
fresh_tomatoes.open_movies_page(movies)
