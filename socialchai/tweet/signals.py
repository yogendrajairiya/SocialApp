from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Tweet, Profile
import os

@receiver(post_delete, sender=Tweet)
def delete_tweet_image(sender, instance, **kwargs):
    if instance.photo and instance.photo.path:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)

@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
