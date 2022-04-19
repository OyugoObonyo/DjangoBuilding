from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE


class Building(models.Model):
    """
    
    A class representing the building table in the db
    """

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    units_count = models.IntegerField() 
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name