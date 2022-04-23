from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

CATEGORY_CHOICES = (
    ('action', 'ACTION'),
    ('drama', 'DRAMA'),
    ('comedy' , 'COMEDY'),
    ('romance', 'ROMANCE')
)

LANGUAGE_CHOICES = (
    ('english', 'ENGLISH'),
    ('germany' , 'GERMANY')
)

STATUS_CHOICES = (
    ('most watched', 'MOST WATCHED'),
    ('recently added','RECENTLY ADDED'),
    ('top rated' , 'TOP RATED')
)

class Movie(models.Model):

    title =  models.CharField(_("title"), max_length=350)
    desc = models.TextField(_("description"))
    # tags = 
    views_count = models.IntegerField(_("views count") , default=0)
    image = models.ImageField(_("image"), upload_to='movies', blank=True , null=True)
    
    # movie banner 
    # banner = models.ImageField(_("banner"), upload_to='banner', blank=True , null=True)

    category = models.CharField(_("category"), choices=CATEGORY_CHOICES  , max_length=30)
    year_of_production = models.DateField(_("year of production") , auto_now_add=False)
    status = models.CharField(_("status"), choices=STATUS_CHOICES  , max_length=30)
    cast = models.CharField(_("cast"), max_length=350)
    langauge = models.CharField(_("language"),choices=LANGUAGE_CHOICES ,max_length=30)
    slug = models.SlugField(_("slug") , blank=True, null=True)
    # todo movie trailor
    movie_trailor = models.URLField(_("movie trailor"))
   

   


    # related_movies = 

    

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug = slugify(self.title)
       return super(Movie, self).save(*args, **kwargs) # Call the real save() method

    
    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"pk": self.pk})
    



LINK_CHOICES = (
    ('D' , 'DOWNLOAD LINK'),
    ('W' , 'WATCH LINK')
)


class MovieLink(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_link', verbose_name=_("movie"), on_delete=models.CASCADE)
    type = models.CharField(_("type"),choices= LINK_CHOICES, max_length=50)
    link = models.URLField(_("link"))
  
    def __str__(self):
        return str(self.movie.title)

    class Meta:
      
        verbose_name = 'MovieLink'
        verbose_name_plural = 'MovieLinks'


