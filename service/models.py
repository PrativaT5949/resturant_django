from django.db import models


# Create your models here.
class Service(models.Model):
    icon_class = models.CharField(
        max_length=100, help_text="FontAwesome icon class, e.g. 'fa-user-tie'"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
