from djongo import models


# Create your models here.
class Setting(models.Model):
    _id = models.ObjectIdField()
    cache_time = models.IntegerField(default=0)

    def __str__(self):
        return str(self.cache_time)
