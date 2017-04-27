#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<year>\d{4})/$',
        views.{{cookiecutter.model|capitalize}}YearArchiveView.as_view(),
        name='{{cookiecutter.model|lower}}_archive_year'
        ),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$',
        views.{{cookiecutter.model|capitalize}}MonthArchiveView.as_view(),
        name='{{cookiecutter.model|lower}}_archive_month'
        ),
    url(r'^(?P<year>[0-9]{4})/(?P<month>\d\d)/(?P<day>\d\d)/$',
        views.{{cookiecutter.model|capitalize}}DayArchiveView.as_view(),
        name='{{cookiecutter.model|lower}}_archive_day'
        ),
    ]
