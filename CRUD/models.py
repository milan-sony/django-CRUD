from django.db import models

# Create your models here.
class register(models.Model):
  name = models.CharField(max_length = 200)
  email = models.EmailField()
  contact = models.IntegerField()

# To give custom table name
  class Meta:
    db_table = 'data'
