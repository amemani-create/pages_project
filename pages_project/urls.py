#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 23:29:30 2021

@author: aditimemani
"""

from django.contrib import admin
from django.urls import path, include # new
urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('pages.urls')), # new
]