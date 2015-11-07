# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dguv3', '0007_safetyclass_two_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='safetyclass_one_device',
            name='pe_voltage',
        ),
        migrations.AddField(
            model_name='safetyclass_one_device',
            name='pe_current',
            field=models.DecimalField(default=-1, max_digits=6, decimal_places=3),
            preserve_default=False,
        ),
    ]
