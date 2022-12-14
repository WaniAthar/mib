from django.db import models
from django.contrib.auth.models import User
import datetime

class Gallery(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    caption = models.TextField(max_length=400)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title

class Update(models.Model):
    title = models.TextField(max_length=500)
    description = models.TextField(max_length=1500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    email = models.EmailField()
    image = models.ImageField(upload_to='team_avatars', blank=True)
    def __str__(self):
        return self.name
    
class PupaVolunteer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    email = models.EmailField()
    image = models.ImageField(upload_to='volunteer_avatars', blank=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1500)
    contact_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    