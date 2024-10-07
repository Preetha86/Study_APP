from django.db import models

class Stud(models.Model):
    Name = models.CharField(max_length=40)
    Phase = models.CharField(max_length=40)
    Sponsor = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
