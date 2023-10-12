using System;
using MongoDB.Driver;
using dotenv.net;

namespace FilmRecommendator
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                DotEnv.Load();

                string mongoURI = Environment.GetEnvironmentVariable("MONGODB_URI");

                MongoClient client = new MongoClient(mongoURI);
            }
            catch (Exception e)
            {
                Console.WriteLine($"Error: {e.Message}");
            }
        }
    }
}