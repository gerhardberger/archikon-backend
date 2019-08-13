from django.db import models


class Award(models.Model):
    name_hu = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    year = models.IntegerField()
    subtitle_hu = models.CharField(max_length=200)
    subtitle_en = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)
