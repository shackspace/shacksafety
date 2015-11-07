# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dguv3', '0006_safetyclass_one_device_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='safetyclass_two_device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('sticker_id', models.IntegerField(help_text=b'number written on the sticker')),
                ('comment', models.CharField(max_length=255, null=True, blank=True)),
                ('visual_inspection', models.BooleanField(default=True)),
                ('iso_resistance', models.DecimalField(help_text=b'Isolation Resistance in Mega-Ohm', max_digits=6, decimal_places=3)),
                ('leakage_current', models.DecimalField(help_text=b'Beruehrungsspannung', max_digits=8, decimal_places=2)),
                ('test_passed', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
