from bson import ObjectId

class Film:
    def __init__(self, id, title, year, director, genre, summary=None):
        self.id = id
        self.title = title
        self.year = year
        self.director = director
        self.genre = genre
        self.summary = summary