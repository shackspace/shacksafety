# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dguv3', '0008_auto_20151107_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='safetyclass_two_device',
            name='iso_resistance',
            field=models.DecimalField(help_text=b'Isolation Resistance in Mega-Ohm', null=True, max_digits=6, decimal_places=3, blank=True),
        ),
        migrations.AlterField(
            model_name='safetyclass_two_device',
            name='leakage_current',
            field=models.DecimalField(help_text=b'Beruehrungsspannung', null=True, max_digits=8, decimal_places=2, blank=True),
        ),
    ]
