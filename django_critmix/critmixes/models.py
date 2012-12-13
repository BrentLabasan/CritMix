from django.db import models

# Create your models here.

class Critmix(models.Model):
  mix_url = models.CharField(max_length=200)
  #pub_date = models.DateTimeField('date published')
  jsonData = models.TextField(default="{'id': 'asdfg', 'start': new Date(2012,5,1,0,0),'content': chee + '<br/>Criticism #1'}")

  def __unicode__(self):
    return self.mix_url

class Crit(models.Model):
  critmix = models.ForeignKey(Critmix)
  comment = models.CharField(max_length=200)
  critique = models.IntegerField()
  position = models.IntegerField()

  def __unicode__(self):
    return self.comment
