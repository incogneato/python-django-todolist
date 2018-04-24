# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)
    text  = models.TextField()
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title;
