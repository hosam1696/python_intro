from projects import movie
from projects import fresh_tomatoes

avengers = movie.Movie(title="Avengers", story_line="Heros movie", post_url="https://www.youtube.com/watch?v=6ZfuNTqbHE8", movie_url="https://www.youtube.com/watch?v=6ZfuNTqbHE8")
hungergames = movie.Movie(title="Hidden", story_line="Action movie", post_url="https://www.youtube.com/watch?v=6ZfuNTqbHE8", movie_url="https://www.youtube.com/watch?v=6ZfuNTqbHE8")


fresh_tomatoes.open_movies_page([avengers, hungergames])