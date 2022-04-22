from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE


class Tag(models.Model):
    """
    
    A class representing the tag table in the database
    """

    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


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
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

 
class Review(models.Model):
    """
    
    A class representing the review table in the database 
    """

    title = models.CharField(max_length=50)
    body = models.CharField(max_length=150)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title