from django.db import models
#from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    descreption = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    views=models.IntegerField(default=0)
    author =models.ForeignKey('auth.User')
    def __unicode__(self):
        return self.title