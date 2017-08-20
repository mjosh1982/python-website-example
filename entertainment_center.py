import media
import fresh_tomatoes

#Create an instance of movie Toy Story
toy_story = media.Movie("Toy Story",
	"A story of a boy and his toys",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=4KPTXpQehio")
# print(toy_story.storyline)

# Create an instance of movie Avatar
avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
	"http://www.youtube.com/watch?v=-9ceBgWV8io")
# print avatar_story.storyline
# avatar.show_trailer()

#Create an instance of movie School of Rock
school_of_rock = media.Movie("School of Rock",
	"Using the rock music to learn",
	"http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
	"https://www.youtube.com/watch?v=3PsUJFEBC74")

#Create an instance of Movie Ratatouille
ratatouille = media.Movie("Ratatouille", 
	"A rat is a checf in Paris",
	"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
	"https://www.youtube.com/watch?v=c3sBBRxDAqk")

#Create an instance of movie Midnight in Paris
midnight_in_paris = media.Movie("Midnight in Paris",
	"Goidn back in time to meet authors",
	"http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
	"https://www.youtube.com/watch?v=atLg2wQQxvU")

#Create an instance of Movie Hunger Games
hunger_games = media.Movie("Hunger Games",
	"A really real reality game",
	"https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
	"https://www.youtube.com/watch?v=PbA63a7HObo")

#Create a list fo movies
movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]

#Open Web page to display the movies on browser with the list of movies
fresh_tomatoes.open_movies_page(movies)

# print media.Movie.VALID_RATINGS