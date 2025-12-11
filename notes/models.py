from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# -----------------------------
# User Profile (Role Handling)
# -----------------------------
class UserProfile(models.Model):
    """
    Extends Django's built-in User model with a role field.
    Roles determine access level inside the app.
    """

    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='user'
    )

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"


# Automatically create a UserProfile whenever a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# -----------------------------
# Notes
# -----------------------------
class Note(models.Model):
    """
    Represents a user-created note.
    Each note belongs to one user, has a title, content,
    and timestamps for creation + last update.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']  # newest edited note at the top

    def __str__(self):
        return self.title
