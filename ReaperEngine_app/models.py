# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL)
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     created_date = models.DateTimeField(blank=True, null=True)
#     published_date = models.DateTimeField(blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __unicode__(selfself):
#         return self.title