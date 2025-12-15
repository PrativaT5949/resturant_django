from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    datetime = models.DateTimeField()
    people = models.PositiveIntegerField()
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.name} for {self.people} people on {self.datetime}"
