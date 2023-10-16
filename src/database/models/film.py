from bson import ObjectId

class Film:
    def __init__(self, title, year, director, genre, summary=None):
        self._id = ObjectId()
        self.title = title
        self.year = year
        self.director = director
        self.genre = genre
        self.summary = summary