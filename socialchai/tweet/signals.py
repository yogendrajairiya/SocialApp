from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Tweet
import os

@receiver(post_delete, sender=Tweet)
def delete_tweet_image(sender, instance, **kwargs):
    if instance.photo and instance.photo.path:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)
