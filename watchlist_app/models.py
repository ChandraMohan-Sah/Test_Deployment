from django.db import models

# Create your models here.

# class StreamPlatform(models.Model):
#     name = models.CharField(max_length=30)
#     about = models.CharField(max_length=150)
#     website = models.URLField(max_length=100)

#     def __str__(self):
#         return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    active = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name 
    
