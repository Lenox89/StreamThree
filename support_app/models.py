# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ReaperEngine_prj.settings import AUTH_USER_MODEL

# Create your models here.
class Ticket(models.Model):
  description = models.TextField("Describe the issue:")
  status = models.CharField(
    max_length = 8,
    choices = (
      ('Pending','Pending'),
      ('Working','Working'),
      ('Complete','Complete')
    ),
    default = 'Pending'
  )
  votes = models.IntegerField(editable=False,default = 0)
  user = models.ForeignKey(AUTH_USER_MODEL,unique=False,blank=True)

  def __unicode__(self):
    return str(self.id)

class Comment(models.Model):
  ticket = models.ForeignKey('Ticket',null=True)
  comment = models.TextField('Type Your Comment Here')
  user = models.ForeignKey(AUTH_USER_MODEL,unique=False,blank=True,null=True)
  date = models.DateField(auto_now_add=True)

class VoteTracker(models.Model):
  ticket = models.ForeignKey('Ticket', unique=False)
  user = models.ForeignKey(AUTH_USER_MODEL, unique=False, blank=True)