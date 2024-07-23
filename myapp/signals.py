from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Followers, Posts, Notifications

@receiver(post_save, sender=Followers)
def create_follow_notification(sender, instance, created, **kwargs):
    if created:
        # Create a follow notification for the followee
        Notifications.create_follow_notification(instance.followee_id, instance.follower_id)

@receiver(post_save, sender=Posts)
def create_post_notification(sender, instance, created, **kwargs):
    if created:
        # Get followers of the user who created the post
        followers = instance.user.followers.all()
        for follower in followers:
            # Create a post notification for each follower
            Notifications.create_post_notification(follower.follower_id, instance.user, instance)
