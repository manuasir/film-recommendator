from database import api
from dotenv import load_dotenv
import os

load_dotenv()

api_instance = api.API(os.getenv("API_KEY"), "https://api.themoviedb.org/3", 1, 5)

try:
    api_instance.insert_films()
except Exception as e:
    print(f"Error: {e}")
