import requests
from dotenv import load_dotenv
from index import conn
from models.film import Film
import os

load_dotenv()

#Clave de la API de TMDb (token)
api_key = "2ffcfdf1b9901801d0659954f796424c"

#URL base de la API de TMDb
base_url = "https://api.themoviedb.org/3"

#Parámetros de la solicitud a la API
params = {
    "api_key": api_key,
}

#ID inicial de película o serie
start_id = 1  

#ID final de película o serie
end_id = 1000  # Puedes aumentar si se requieren mas cantidad de peliculas

for movie_id in range(start_id, end_id + 1):
    #solicitud a la API de TMDb para obtener información de una película o serie
    response = requests.get(f"{base_url}/movie/{movie_id}", params=params)

    #Comprobar si la solicitud fue exitosa(En el protocolo HTTP, el código de estado "200 OK" indica que la solicitud fue exitosa)
    if response.status_code == 200:
        #Procesar los datos de la película o serie
        movie_data = response.json()

        #Crear un objeto Film con los datos necesarios
        film = Film(
            title=movie_data["title"],
            year=movie_data["release_date"].split("-")[0],
            director=movie_data["director"],  #obtener el director desde la API
            genre=movie_data["genres"],  #obtener los géneros desde la API
            summary=movie_data.get("overview", "")  #Resumen de la película
        )

        # Insertar el objeto Film en la base de datos MongoDB
        conn.coll.insert_one(film.__dict__)

print("Datos insertados en la base de datos.")
