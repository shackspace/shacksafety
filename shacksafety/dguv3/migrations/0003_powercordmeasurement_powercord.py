# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dguv3', '0002_auto_20151106_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='powercordmeasurement',
            name='powercord',
            field=models.ForeignKey(default=1, to='dguv3.Powercord'),
            preserve_default=False,
        ),
    ]
