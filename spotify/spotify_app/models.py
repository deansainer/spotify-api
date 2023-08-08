from django.db import models


class Uri(models.Model):
    uri = models.CharField(max_length=500, blank=False, null=False)