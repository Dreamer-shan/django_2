# Generated by Django 2.2.1 on 2019-11-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('things', models.CharField(max_length=50)),
                ('done', models.BooleanField(default=False)),
                ('things_2', models.CharField(max_length=100)),
            ],
        ),
    ]
