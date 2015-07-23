# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Behaviour',
            fields=[
                ('behaviour_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('behaviour', models.ForeignKey(to='studentApp.Behaviour')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
                ('student_class', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='point',
            name='student',
            field=models.ForeignKey(to='studentApp.Student'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(to='studentApp.Student'),
        ),
    ]
