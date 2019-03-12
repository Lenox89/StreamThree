# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Donations(models.Model):
    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]
    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in range(19, 36)]

    card = models.CharField('Credit card number',max_length=19)
    code = models.CharField('Security code (CVV)', max_length=4)
    month = models.CharField("Month", choices=MONTH_CHOICES, max_length=3)
    year = models.CharField("Year", choices=YEAR_CHOICES, max_length=4)