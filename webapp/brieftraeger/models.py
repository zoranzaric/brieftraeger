from django.db import models
from django.contrib.sites.models import Site

class List(models.Model):
    name = models.CharField(max_length=200)
    site = models.ForeignKey(Site)

    def __unicode__(self):
        return "%s@%s" % (self.name, self.site.domain)

class Subscriber(models.Model):
    email = models.EmailField()
    list = models.ForeignKey(List)

    def __unicode__(self):
        return self.email

class Email(models.Model):
    message_id = models.CharField(max_length=255)
    list = models.ForeignKey(List, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    message = models.TextField()

