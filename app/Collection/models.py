from django.contrib.auth.models import User
from django.db import models


class Collection(models.Model):
    """
    Model for storing collections.

    Attributes:
        name (CharField): The name of the collection.
        description (TextField, optional): Brief description of the collection.
        created_at (DateTimeField): Date and time the collection was created.
        updated_at (DateTimeField): Date and time the collection was last updated.

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
