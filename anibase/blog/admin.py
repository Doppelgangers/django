from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Artwork)
admin.site.register(AlternativeName)
admin.site.register(CategoryArtwork)
admin.site.register(SeriesArtwork)
admin.site.register(Author)
