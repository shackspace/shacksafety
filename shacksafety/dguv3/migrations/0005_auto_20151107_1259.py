# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dguv3', '0004_auto_20151107_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='safetyclass_one_device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('sticker_id', models.IntegerField(help_text=b'number written on the sticker')),
                ('visual_inspection', models.BooleanField(default=True)),
                ('iso_resistance', models.DecimalField(help_text=b'Isolation Resistance in Mega-Ohm', max_digits=6, decimal_places=3)),
                ('pe_resistance', models.DecimalField(help_text=b'PE Resistance in milli-Ohm', max_digits=6, decimal_places=3)),
                ('pe_voltage', models.DecimalField(help_text=b'PE Resistance in milli-Ohm', max_digits=6, decimal_places=3)),
                ('test_passed', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='safetyclass_one',
        ),
    ]
