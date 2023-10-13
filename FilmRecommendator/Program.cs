// Import necessary namespaces
using dotenv.net;
using Controllers;

namespace Program
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Load environment variables from .env file
                DotEnv.Load();

                // Retrieve the MongoDB URI from environment variables
                string mongoURI = Environment.GetEnvironmentVariable("mongoURI");

                // Create an instance of the Controller class, passing the MongoDB URI
                Controller ctrl = new Controller(mongoURI);

                // Example of using the addFilm method
                // ctrl.addFilm("Blade Runner", 1982, "Ridley Scott", "Sci-Fi", null);

            }
            catch (Exception e)
            {
                // Handle any exceptions that may occur and display an error message
                Console.WriteLine($"Error: {e.Message}");
            }
        }
    }
}
