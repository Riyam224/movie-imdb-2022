from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 
from django.views.generic import ListView , DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie , MovieLink

class HomeView(ListView):
    model  = Movie
    template_name = 'movieImdb/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["top_rated"] = Movie.objects.filter(status='top rated')
        context["most_watched"] = Movie.objects.filter(status='most watched')
        context["recently_added"] = Movie.objects.filter(status='recently added')
        return context
    


class MovieList(ListView):
    model  = Movie
    paginate_by = 2


class MovieDetail(DetailView):
    model = Movie
    template_name = "movieImdb/movie_detail.html"


    def get_object(self):
        object = super(MovieDetail , self).get_object()
        # todo add views by one 
        object.views_count += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["links"] = MovieLink.objects.filter(movie=self.get_object())
        context['related_movies'] = Movie.objects.filter(category=self.get_object().category)
        return context
    



class MovieCategory(ListView):

    model = Movie
    paginate_by = 1


    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)


    def get_context_data(self, **kwargs):
        context = super(MovieCategory , self).get_context_data(**kwargs)
        context["movie_category"] = self.category
        return context
    
    


class MovieLanguage(ListView):
    model = Movie
    paginate_by = 1


    def get_queryset(self):
        self.langauge = self.kwargs['langauge']
        return Movie.objects.filter(langauge=self.langauge)


    def get_context_data(self, **kwargs):
        context = super(MovieLanguage,self).get_context_data(**kwargs)
        context["movie_language"] = self.langauge
        return context



class MovieSearch(ListView):
    model = Movie
    paginate_by = 1



    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
            print(query)
            print(object_list)
        
        else:
            object_list = self.model.objects.none()

        return object_list


class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True
    print(queryset)
    
    
    

