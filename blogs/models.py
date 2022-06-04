from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    owner = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
