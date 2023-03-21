from django.db import models

# Create your models here.

class Rezyser(models.Model):
    name=models.CharField(max_length=65)
    country=models.CharField(max_length=46)

    def get_last_films(self):
        return self.films.all().last()

class Film(models.Model):
    rezyser=models.ForeignKey(Rezyser, on_delete=models.CASCADE, related_name="movies")
    tytul=models.CharField(max_length=64)