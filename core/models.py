from django.db import models


class Keyword(models.Model):
    keyword = models.CharField(unique=True, max_length=300)
    hits = models.IntegerField(default=0)

    def __unicode__(self):
        return self.keyword
