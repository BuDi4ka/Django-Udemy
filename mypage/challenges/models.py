from django.db import models
from django.db.models import AutoField


# Create your models here.
class Book(models.Model):
    id = AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=50)
    rating = models.Field()
