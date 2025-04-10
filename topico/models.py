from django.db import models

# Create your models here.
class topicModel(models.Model):
    nome=models.CharField(max_length=30, null=False)
    password= models.CharField(null=False,blank=False)
    