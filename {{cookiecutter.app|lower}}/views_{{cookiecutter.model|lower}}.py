#!/usr/bin/env python
# -*- coding: utf-8 -*-
{% set app=cookiecutter.app|lower -%}
{% set App=cookiecutter.app|capitalize -%}
{% set model=cookiecutter.model|lower -%}
{% set Model=cookiecutter.model|capitalize -%}
{% set fecha=cookiecutter.fecha|lower -%}

from django.urls import reverse_lazy
from comun.filters import as_mes, as_fecha
from comun.web import Webo

from {{app}} import models

class {{Model}}Archive:

    queryset = models.{{Model}}.objects.all()
    month_format = '%m' 
    date_field = "{{fecha}}"
    allow_future = True

    def link_to_year(self, year):
        return (
            year,
            reverse_lazy(
                '{{app}}:{{model}}_archive_year',
                kwargs={'year': str(year)}
                )
            )

    def link_to_month(self, year, month):
        return (
            as_mes(month),
            reverse_lazy(
                '{{app}}:{{model}}_archive_month',
                kwargs={
                    'year': str(year),
                    'month': '{:02d}'.format(month),
                    }
                )
            )

    def link_to_day(self, year, month, day):
        return (
            day,
            reverse_lazy(
                '{{app}}:{{model}}_archive_day',
                kwargs={
                    'year': str(year),
                    'month': '{:02d}'.format(month),
                    'day': '{:02d}'.format(day),
                    }
                )
            )


class {{Model}}YearArchiveView({{Model}}Archive, YearArchiveView):

    def render_to_response(self, context, **kwargs):
        f_ref = context['year']
        year = f_ref.year
        page = Webo(self.request, self.get_template_names(), context)
        page.breadcrumb(*ROOT)
        page.breadcrumb(*self.link_to_year(year))
        return page.render(
            titulo='{{Model}} / Año {}'.format(year),
            )


class {{Model}}MonthArchiveView({{Model}}Archive, MonthArchiveView):

    def render_to_response(self, context, **kwargs):
        f_ref = context['month']
        year, month = f_ref.year, f_ref.month
        page = Webo(self.request, self.get_template_names(), context)
        page.breadcrumb(*ROOT)
        page.breadcrumb(*self.link_to_year(year))
        page.breadcrumb(*self.link_to_month(year, month))
        return page.render(
            titulo='{{Model}} {}/{}'.format(year, month),
            )


class {{Model}}DayArchiveView({{Model}}Archive, DayArchiveView):

    def render_to_response(self, context, **kwargs):
        f_ref = context['day']
        year, month, day = f_ref.year, f_ref.month, f_ref.day
        page = Webo(self.request, self.get_template_names(), context)
        page.breadcrumb(*ROOT)
        page.breadcrumb(*self.link_to_year(year))
        page.breadcrumb(*self.link_to_month(year, month))
        page.breadcrumb(*self.link_to_day(year, month, day))
        return page.render(
            titulo='{{Model}} / fecha {}'.format(as_fecha(f_ref)),
            )

