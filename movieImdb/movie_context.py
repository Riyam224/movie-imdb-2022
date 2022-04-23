from .models import Movie


def slider_movies(request):
    movies = Movie.objects.all()
    return {'slider_movie': movies }