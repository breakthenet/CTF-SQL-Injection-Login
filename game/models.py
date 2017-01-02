from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')

    def __unicode__(self):
        return u'%s' % (self.code, self.name)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
