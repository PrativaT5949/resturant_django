from django.db import models


# Create your models here.
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="testimonials/")
    message = models.TextField()

    def __str__(self):
        return self.client_name
