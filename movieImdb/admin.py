from django.contrib import admin

# Register your models here.
from .models import Movie , MovieLink


admin.site.register(Movie)
admin.site.register(MovieLink)