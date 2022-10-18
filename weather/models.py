from djongo import models


class Setting(models.Model):
    _id = models.ObjectIdField()
    cache_time = models.IntegerField(default=0)

    def __str__(self):
        return str(self.cache_time)
