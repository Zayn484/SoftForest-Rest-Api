from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from accounts.models import Profile
User = settings.AUTH_USER_MODEL

# Create your models here.


class Friend(models.Model):
    user = models.OneToOneField(User, related_name='creator', on_delete=models.CASCADE)
    members = models.ManyToManyField(Profile, blank=True)

    def __str__(self):
        return str(self.user.username)


class Invitation(models.Model):
    user = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    recipient = models.PositiveIntegerField()
    accepted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=Invitation)
def new_invitation(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "invite", {
                "type": "user.invite",
                "event": "New invitation",
                "user": instance.user.username,
                "recipient": instance.recipient
            }
        )



