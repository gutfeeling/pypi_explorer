from django.db import models

# Create your models here.

class PackageInfo(models.Model):

    name = models.TextField()
    has_classifiers = models.BooleanField()
    python3_compatible = models.BooleanField()
    total_downloads = models.IntegerField()
    #description_length = models.IntegerField(null = True)
    #number_of_releases = models.IntegerField()
    last_release_date = models.DateField(null = True)
    last_release_size_source = models.IntegerField(null = True)
    last_release_size_wheel = models.IntegerField(null = True)
    development_status = models.CharField(max_length = 100, null = True)
    #quality_factor = models.FloatField(null = True)
    #first_release_date = models.DateField(null = True)
    keywords = models.TextField(null = True)

    def __str__(self):
        return self.name
