from django.contrib import admin
from .models import Tag, Startup, NewsLink

admin.site.register([Tag, Startup, NewsLink])
