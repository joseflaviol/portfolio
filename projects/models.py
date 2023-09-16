from django.db import models
from django.contrib import admin

class Project(models.Model):

    title       = models.CharField(max_length = 30)
    subtitle    = models.CharField(max_length = 255)
    description = models.TextField()
    reference   = models.CharField(max_length = 255)

admin.site.register(Project)