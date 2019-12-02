from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(default='default.jpg', upload_to='profile_pics')   

    def __str__(self):
        return f'{self.user.username} Profile'

#must register our models in admin.py after we make migrations
#this creates a folder called profile_pics. 
#However, it will be messy to keep everything here so we are creating a new directory

#We will override the save method to size our image
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
