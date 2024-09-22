from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

class Friend(models.Model):
    user_from = models.ForeignKey(User, related_name='friend_from', on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='friend_to', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)