from django.contrib import admin
from .models import Film
# Register your models here.

#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields = ["title", "description"]
    #exclude = ["description"]
    list_display = ["title", "rating", "year"]
    list_filter= ["title"]
    search_fields=["title"]