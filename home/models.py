from django.core.exceptions import ValidationError
from django.db import models


class HomePage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    button_text = models.CharField(max_length=50, default="Book A Table")
    button_link = models.CharField(max_length=100, default="#booking")
    image = models.ImageField(
        upload_to="hero_images/", blank=True, null=True, help_text="Hero section image"
    )

    def save(self, *args, **kwargs):
        if not self.pk and HomePage.objects.exists():
            raise ValidationError(message="Only one HomePage instance is allowed.")
        super().save(*args, **kwargs)

    def __str__(self):
        return "HomePage Content"
