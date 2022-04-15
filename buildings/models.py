from django.db import models


class Building(models.Model):
    """
    
    A class representing the building table in the db
    """

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    units_count = models.IntegerField
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Building id:{self.id}, Building name: {self.name}"