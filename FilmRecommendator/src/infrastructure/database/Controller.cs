using MongoDB.Driver;
using Models;

namespace Controllers
{
    public class Controller
    {
        private string URI;

        private MongoClient client;

        public Controller(string URI)
        {
            this.URI = URI;
            client = new MongoClient(this.URI);
        }

        public void addFilm(string Title, int Year, string Director, string Genre, string Summary)
        {
            var database = client.GetDatabase("FilmRecommendator");

            var collection = database.GetCollection<Film>("Films");

            var newFilm = new Film
            {
                Title = Title,
                Year = Year,
                Director = Director,
                Genre = Genre,
                Summary = Summary
            };

            collection.InsertOne(newFilm);
        }
    }
}
