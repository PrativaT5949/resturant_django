from django.db import models


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200, default="Welcome to Restoran")
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description1 = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    years_experience = models.PositiveIntegerField(default=15)
    popular_chefs = models.PositiveIntegerField(default=50)
    read_more_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
