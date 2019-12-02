from django.db.models.signals import post_save
#signal that gets fired after an object is saved. We want a signal when a user is created
from django.contrib.auth.models import User
#User model is the sender
#also need a receiver
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

#need to go to apps.py after