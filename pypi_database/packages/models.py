from django.db import models

# Create your models here.


class Package(models.Model):

    name = models.TextField()
    metadata = models.TextField()

    def __str__(self):
        return self.name
