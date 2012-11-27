from django.db import models
import soundcloud

client = soundcloud.Client(client_id='4d9fea6bff39bf127b10e87a2f478aea')

# Create your models here.

class Critmix(models.Model):
  mix_url = models.CharField(max_length=200)
  #pub_date = models.DateTimeField('date published')

  def __unicode__(self):
    return self.mix_url

class Crit(models.Model):
  critmix = models.ForeignKey(Critmix)
  comment = models.CharField(max_length=200)
  critique = models.IntegerField()
  position = models.IntegerField()

  def __unicode__(self):
    return self.comment
