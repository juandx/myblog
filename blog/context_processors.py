#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from . import models
from django.db.models import Count
def custom_proc(request):
    categories = models.Category.objects.annotate(
        num_post=Count('post')).filter(num_post__gt=0).order_by('name')
    return {
        'CATEGORIES': categories,
    }

