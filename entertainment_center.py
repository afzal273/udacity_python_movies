import media
import fresh_tomatoes

__author__ = 'Afzal Syed'

# Making movie objects from the media module

paddington = media.Movie(771366608,
                         "https://upload.wikimedia.org/wikipedia/en/0/06/PaddingtonPOSTER.jpg",
                         "https://www.youtube.com/watch?v=qFuzMlfZGWM")

mad_max_fury = media.Movie(771028170,
                           "https://upload.wikimedia.org/wikipedia/en/thumb/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg/220px-Max_Mad_Fury_Road_Newest_Poster.jpg",
                           "https://www.youtube.com/watch?v=hEJnMQG9ev8")

inside_out = media.Movie(771306118,
                         "https://upload.wikimedia.org/wikipedia/en/thumb/0/0a/Inside_Out_%282015_film%29_poster.jpg/220px-Inside_Out_%282015_film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=seMwpP0yeu4")

interstellar = media.Movie(771351912,
                           "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Interstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=2LqzF5WauAw")

big_hero_6 = media.Movie(771355766,
                         "https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/Big_Hero_6_%28film%29_poster.jpg/220px-Big_Hero_6_%28film%29_poster.jpg",
                         "https://www.youtube.com/watch?v=z3biFxZIJOQ")

peabody_sherman = media.Movie(771169232,
                              "https://upload.wikimedia.org/wikipedia/en/thumb/5/58/Mr_Peabody_%26_Sherman_Poster.JPG/220px-Mr_Peabody_%26_Sherman_Poster.JPG",
                              "https://www.youtube.com/watch?v=hy6oD7BZw50")

# Append each movie to the movies list
movies = [paddington, mad_max_fury, inside_out,
          interstellar, big_hero_6, peabody_sherman]

# Create and open the movies page
fresh_tomatoes.open_movies_page(movies)
