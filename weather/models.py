from django.db import models


# Create your models here.
class Setting(models.Model):
    is_active = models.BooleanField(default=True)
    cache_time = models.IntegerField(default=0)

    def __str__(self):
        return str(self.cache_time)
