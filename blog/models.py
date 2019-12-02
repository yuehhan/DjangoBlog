from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #dont want to execute this function at this point
    #User and Post have a one-to-many relationship
    #Second argument is to delete all posts if user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    #create get absolute url method to let django find a new post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
