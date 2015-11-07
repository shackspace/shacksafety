# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dguv3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PowercordMeasurement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('iso_resistance', models.DecimalField(help_text=b'Isolation Resistance in Mega-Ohm', max_digits=6, decimal_places=3)),
                ('pe_resistance', models.DecimalField(help_text=b'PE Resistance in milli-Ohm', max_digits=6, decimal_places=3)),
                ('visual_inspection', models.BooleanField(default=False, help_text=b'has the device passed the visual inspection?')),
                ('test_passed', models.BooleanField(default=False, help_text=b'has the device passed the test?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='powercord',
            name='iso_resistance',
        ),
        migrations.RemoveField(
            model_name='powercord',
            name='pe_resistance',
        ),
        migrations.RemoveField(
            model_name='powercord',
            name='test_passed',
        ),
        migrations.RemoveField(
            model_name='powercord',
            name='visual_inspection',
        ),
    ]
