from django.contrib.auth.models import User
from django.db import models
from Collection.models import Collection


class Link(models.Model):
    """
    Model for storing user links.
    Attributes:
        user (ForeignKey): The user to whom the link belongs.
        title (CharField): The title of the page.
        description (TextField): Brief description of the page.
        url (URLField): Link to the page.
        image (URLField): Link to the image.
        link_type (IntegerField): Type of the link. Chosen from the predefined list LEVEL_OF_LINK.
        created_at (DateTimeField): Date and time the link was created.
        updated_at (DateTimeField): Date and time the link was last updated.
        collections (ManyToManyField): Collections to which the link belongs.
    """

    LEVEL_OF_LINK = [
        (1, 'website'),
        (2, 'book'),
        (3, 'article'),
        (4, 'music'),
        (5, 'video'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    url = models.URLField(null=False)
    image = models.URLField(null=True)
    link_type = models.IntegerField(choices=LEVEL_OF_LINK, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    collections = models.ManyToManyField(Collection, related_name='links')

    class Meta:
        unique_together = ('user', 'url')  # check links are unique per user
