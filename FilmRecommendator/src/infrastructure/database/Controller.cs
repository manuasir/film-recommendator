// Import necessary namespaces
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
            client = new MongoClient(this.URI); // Create a new MongoDB client using the provided URI
        }

        public void addFilm(string Title, int Year, string Director, string Genre, string Summary)
        {
            // Get a reference to the "FilmRecommendator" database in MongoDB
            var database = client.GetDatabase("FilmRecommendator");

            // Get a reference to the "Films" collection within the database
            var collection = database.GetCollection<Film>("Films");

            // Create a new Film object with the provided data
            var newFilm = new Film
            {
                Title = Title,
                Year = Year,
                Director = Director,
                Genre = Genre,
                Summary = Summary
            };

            // Insert the new Film document into the "Films" collection
            collection.InsertOne(newFilm);
        }
    }
}
