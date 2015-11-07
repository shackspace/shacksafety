# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dguv3', '0005_auto_20151107_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='safetyclass_one_device',
            name='comment',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
