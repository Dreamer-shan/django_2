# Generated by Django 2.2.1 on 2019-11-28 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='things_2',
        ),
    ]
