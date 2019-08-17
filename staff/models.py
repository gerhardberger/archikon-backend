from django.db import models


class Staff(models.Model):
    name = models.CharField(max_length=40)
    title_hu = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=100)
    leader = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='staff/', null=True, blank=True)

    def __str__(self):
        return str(self.id)
