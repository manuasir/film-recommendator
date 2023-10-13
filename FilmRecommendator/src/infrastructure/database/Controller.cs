using MongoDB.Driver;

namespace Controllers
{
    public class Controller
    {
        public string URI;

        public Controller(string URI)
        {
            this.URI = URI;
        }

        public MongoClient clientConnection()
        {
            return new MongoClient(this.URI);
        }
    }
}
