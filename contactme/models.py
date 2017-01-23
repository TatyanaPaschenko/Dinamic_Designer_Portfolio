from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    message = models.CharField(max_length= 400)
    email = models.EmailField()
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
