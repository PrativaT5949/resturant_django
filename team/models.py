from django.db import models


# Create your models here.
class TeamMember(models.Model):
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="team_photos/")
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name
