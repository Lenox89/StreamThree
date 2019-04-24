# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Ticket
from django.contrib import admin

# Register your models here.
def make_todo(ModelAdmin,request, queryset):
  queryset.update(status='Pending')
make_todo.short_description = "Mark selected as pending"

def make_doing(ModelAdmin,request, queryset):
  queryset.update(status='Working')
make_doing.short_description = "Mark selected as working"

def make_done(ModelAdmin,request, queryset):
  queryset.update(status='Complete')
make_done.short_description = "Mark selected as complete"

class Admin_Ticket(admin.ModelAdmin):
  list_display = ['id','issue','type','status','user','modified']
  list_editable = ['status','type']
  date_hierarchy = 'modified'
  # date_hierarchy= 'modified'
  actions = [make_done,make_doing,make_todo]

admin.site.register(Ticket,Admin_Ticket)