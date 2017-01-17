from django.utils import timezone
from django.db import models


class PhotoModel(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    mini_image_title = models.ImageField(upload_to='images/', height_field=None, width_field=None)
    first_image_comp = models.ImageField(upload_to='images/', height_field=None, width_field=None)
    first_or_lending_image = models.ImageField(upload_to='images/', height_field=None, width_field=None)
    second_image = models.ImageField(upload_to='images/', height_field=None, width_field=None)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    from_email = models.EmailField()
    create_date = models.DateField(auto_now=True)