# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enrollmentnumber', models.IntegerField()),
                ('gender', models.CharField(max_length=6, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Other', b'Other')])),
                ('branch', models.CharField(max_length=3, choices=[(b'CSE', b'Computer Science'), (b'ECE', b'CElectronics'), (b'EE', b'Electrical'), (b'ME', b'Mechanical'), (b'CHE', b'Chemical'), (b'CE', b'Civil'), (b'PHY', b'Physics')])),
                ('dob', models.DateField()),
                ('about', models.CharField(max_length=500)),
                ('username', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
