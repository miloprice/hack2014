# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20141102_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned',
        ),
    ]
