# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_tag_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='priority',
        ),
        migrations.DeleteModel(
            name='Priority',
        ),
    ]
