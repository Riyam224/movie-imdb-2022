from django.urls import path 
from . import views 





urlpatterns = [
    path("", views.MovieList.as_view(), name="movie_list"),
    path('category/<str:category>/' , views.MovieCategory.as_view() , name='movie_category'),
    path("language/<str:langauge>/", views.MovieLanguage.as_view(), name="movie_language"),
    path("search/", views.MovieSearch.as_view(), name="movie_search"),
    path("year/<int:year>/", views.MovieYear.as_view(), name="movie_year"),
    path('<int:pk>/' , views.MovieDetail.as_view() , name='movie_detail'),
    
]
