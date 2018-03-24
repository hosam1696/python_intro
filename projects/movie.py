class Movie():
    """
        title
        story line
        image url
        trailor youtube url
    """

    def __init__(self, title, story_line, post_url, movie_url):
        self.title = title
        self.story_line = story_line
        self.post_url = post_url
        self.movie_url = movie_url


toy_story = Movie(title="Toy Story", story_line="animation movie", post_url="fsdfsdf", movie_url="fsdffsd")

print(toy_story.title)
