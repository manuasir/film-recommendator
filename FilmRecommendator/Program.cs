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
                DotEnv.Load();

                string mongoURI = Environment.GetEnvironmentVariable("mongoURI");

                Controller ctrl = new Controller(mongoURI);

            }
            catch (Exception e)
            {
                Console.WriteLine($"Error: {e.Message}");
            }
        }
    }
}
