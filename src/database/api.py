from database import connection
from database.models import film
import requests
import os

class API:
    def __init__(self, api_key, base_url, start_id, end_id):
        self.api_key = api_key
        self.base_url = base_url
        self.params = {"api_key": self.api_key}
        self.start_id = start_id
        self.end_id = end_id

    def insert_films(self):
        try:
            conn = connection.Database(
                os.getenv("DB_URI"), os.getenv("DB_NAME"), os.getenv("DB_COLL")
            )
            for movie_id in range(self.start_id, self.end_id + 1):
                # solicitud a la API de TMDb para obtener información de una película o serie
                response = requests.get(f"{self.base_url}/movie/{movie_id}", params=self.params)
                # PENDIENTE
                # solicitud de créditos para extraer al director
                # credits = requests.get(f"{self.base_url}/movie/{movie_id}/credits", params=self.params)
                # Comprobar si la solicitud fue exitosa (En el protocolo HTTP, el código de estado "200 OK" indica que la solicitud fue exitosa)
                if response.status_code == 200:
                    # Procesar los datos de la película o serie
                    movie_data = response.json()
                    # Crear un objeto Film con los datos necesarios
                    sample = film.Film(
                        title=movie_data["title"],
                        year=movie_data["release_date"].split("-")[0],
                        director=movie_data["director"], # PENDIENTE
                        genre=movie_data["genres"],  # obtener los géneros desde la API
                        summary=movie_data.get("overview", "")  # Resumen de la película
                    )
                    # Insertar el objeto Film en la base de datos MongoDB
                    conn.coll.insert_one(sample.__dict__)
                    print("Datos insertados en la base de datos.")
        except Exception as e:
            print(f"Error: {e}")
