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
            # Conexión con MongoDB
            conn = connection.Database(
                os.getenv("DB_URI"), os.getenv("DB_NAME"), os.getenv("DB_COLL")
            )
            for movie_id in range(self.start_id, self.end_id + 1):
                # Solicitud a la API de TMDb para obtener información de una película
                    detail_response = requests.get(f"{self.base_url}/movie/{movie_id}", params=self.params)
                    # Comprobar si la solicitud fue exitosa (En el protocolo HTTP, el código de estado "200 OK" indica que la solicitud fue exitosa)
                    if detail_response.status_code == 200:
                        detail_film = detail_response.json()
                        # solicitud a la API de TMDb para obtener créditos de una película
                        credit_response = requests.get(f"{self.base_url}/movie/{movie_id}/credits", params=self.params)
                        # Comprobar si la solicitud fue exitosa (En el protocolo HTTP, el código de estado "200 OK" indica que la solicitud fue exitosa)
                        if credit_response.status_code == 200:
                            credit_film = credit_response.json()
                        # Crear un objeto Film con los datos necesarios
                        sample = film.Film(
                            title=detail_film["title"], # Obtener título de la película
                            year=detail_film["release_date"].split("-")[0],
                            director=credit_film["crew"][0]["name"],  # Obtener director del objeto "crew"
                            genre=detail_film["genres"],  # Obtener los géneros desde la API
                            summary=detail_film.get("overview", "")  # Obtener resumen de la película
                            )
                        # Insertar el objeto Film en la base de datos MongoDB
                        conn.coll.insert_one(sample.__dict__)
                        print("Datos insertados en la base de datos.")
        except Exception as e:
            print(f"Error: {e}")
    

    def recommend_film(self):
         try:
             
             #coneccion a BD
             conn = connection.Database(os.getenv("DB_URI"), os.getenv("DB_NAME"), os.getenv("DB_COLL"))

             #Obtener una lisa de todas las peliculas
             movies = conn.coll.find()

             #solicitar input del usuario
             user_input = input("Ingrese el titulo de su pelicula preferida")

             #Realizar una busqueda en la base de dato para encontrar peliculas similares
             similar_movies = []

             for movie in movies:
                  if user_input in movie["year"] and user_input.lower() in movie["genre"]:
                       similar_movies.append(movie)
            
            #Mostrar la recomendaccion al usuario
             if similar_movies:
              print("===============Peliculas Recomendadas====================")
              for movie in similar_movies:
                  print(movie["title"])
             else:
                 print("No se encuantran ninguna pelicula de su gusto en nuestra coleccion")

         except Exception as e:
             print(f"A ocurrido un error: {e}")


