from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'content_type', 'object_id')
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    likes = GenericRelation(Like)

    def is_liked_by(self, user):
        return self.likes.filter(user=user).exists()

    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return f"{self.user.username}: {self.text[:10]}..."  # Display first 20 characters of the tweet content
    
class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=60)
    attached_photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = GenericRelation(Like)

    def __str__(self):
        return f"{self.user.username} on {self.tweet.id}: {self.text[:10]}..."  # Display first 20 characters of the comment content

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
    
