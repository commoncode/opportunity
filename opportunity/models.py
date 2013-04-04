from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=240)

    class Meta:
        ordering = ('name', )

    def get_absolute_url(self):
        return reverse('client_detail', args=(self.pk, ))

    def __unicode__(self):
        return (u'%s' % self.name)


class Opportunity(models.Model):
    client = models.ForeignKey('opportunity.Client', related_name='opportunities')
    skills = models.ManyToManyField('opportunity.Skill', related_name='opportunities')

    class Meta:
        ordering = ('pk', )
        verbose_name_plural = 'opportunities'

    def get_absolute_url(self):
        return reverse('opportunity_detail', args=(self.pk, ))

    def __unicode__(self):
        return (u'%s' % self.client.name)


class Resource(models.Model):
    name = models.CharField(max_length=240)
    skills = models.ManyToManyField('opportunity.Skill', related_name='developers')

    class Meta:
        ordering = ('name', )

    def get_absolute_url(self):
        return reverse('resource_detail', args=(self.pk, ))

    def __unicode__(self):
        return (u'%s' % self.name)


class Skill(models.Model):
    name = models.CharField(max_length=240)

    class Meta:
        ordering = ('name', )

    def __unicode__(self):
        return (u'%s' % self.name)
