from django.db import models

# Create your models here.
class AddMaterial(models.Model):
    path = models.ImageField(upload_to="img/")
    nome = models.CharField(max_length=200)
    valor =  models.DecimalField(max_digits=10,decimal_places=2)
