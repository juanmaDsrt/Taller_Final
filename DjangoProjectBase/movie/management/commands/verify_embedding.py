from django.core.management.base import BaseCommand
from movie.models import Movie
import numpy as np
import random

class Command(BaseCommand):
    help = "Muestra los embeddings de una película seleccionada al azar"

    def handle(self, *args, **kwargs):
        movies = list(Movie.objects.all())
        if not movies:
            self.stdout.write(self.style.ERROR("No hay películas en la base de datos."))
            return

        movie = random.choice(movies)  # Selecciona una película al azar
        embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)
        self.stdout.write(self.style.SUCCESS(f"Película: {movie.title}"))
        self.stdout.write(f"Embedding (primeros 5 valores): {embedding_vector[:5]}")
