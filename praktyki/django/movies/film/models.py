from django.db import models

# Create your models here.

class Film(models.Model):
    title=models.CharField(max_length=30, default="")
    director=models.CharField(max_length=30, default="")
    year=models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    country=models.CharField(max_length=30, default="")
    description=models.TextField(default="")
    premiere=models.DateField(null=True, blank=True)
    rating=models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    plakat=models.ImageField(upload_to="plakaty", null=True, blank=True)

    
    def __str__(self):
        return self.tytul_z_rokiem()
    
    def tytul_z_rokiem(self):
        return "{} ({})".format(self.title, self.year)
    

#     def get_last_films(self):
#         return self.films.all().last()

# class Film(models.Model):
#     rezyser=models.ForeignKey(Rezyser, on_delete=models.CASCADE, related_name="movies")
#     tytul=models.CharField(max_length=64)