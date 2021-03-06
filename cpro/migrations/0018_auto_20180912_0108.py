# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-09-12 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cpro', '0017_auto_20180830_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='_cache_owner_email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='i_skill',
            field=models.PositiveIntegerField(choices=[(0, 'Lesser Perfect Lock'), (1, 'Greater Perfect Lock'), (2, 'Extreme Perfect Lock'), (3, 'Combo Lock'), (4, 'Healer'), (5, 'Life Lock'), (6, 'Combo Bonus'), (7, 'Perfect Score Bonus'), (8, 'Overload'), (9, 'Score Boost'), (10, 'All Round'), (11, 'Concentration'), (12, 'Skill Boost'), (13, 'Cute/Cool/Passion Focus'), (14, 'Encore'), (15, 'Life Sparkle'), (16, 'Tricolor Synergy'), (17, 'Focus')], null=True, verbose_name='Skill'),
        ),
    ]
