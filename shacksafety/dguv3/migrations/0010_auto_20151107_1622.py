# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dguv3', '0009_auto_20151107_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safetyclass_one_device',
            name='iso_resistance',
            field=models.DecimalField(help_text=b'Isolation Resistance in Mega-Ohm', null=True, max_digits=6, decimal_places=3, blank=True),
        ),
    ]
