# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Journal(models.Model):
    """Journal Model."""
    class Meta(object):
        verbose_name = u"Журнал"

    present_student = models.OneToOneField('Student_name')

    date = models.DateField(
        blank = False)

    present = models.BooleanField(
        blank = True)
