from django.db import models


class Cable(models.Model):

    def __unicode__(self):
        return ("%s, %s") % (self.id, self.title)

    ref = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    length = models.IntegerField()
    port1 = models.CharField(max_length=200, blank=True, null=True)
    port2 = models.CharField(max_length=200, blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)