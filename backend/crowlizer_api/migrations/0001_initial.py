# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-04 06:50
from __future__ import unicode_literals

from django.db import migrations


def load_sql(filename):
    f = open(filename, encoding='utf-8')
    sql_statements = f.read()
    f.close()
    return sql_statements


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.RunSQL(load_sql('./crowlizer_api/migrations/resources/sql/V1__init_tables.sql'))
    ]
