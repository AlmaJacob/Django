from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Movie)
admin.site.register(Lang)
admin.site.register(movie_lang)

