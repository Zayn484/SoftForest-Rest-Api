# Generated by Django 2.1.7 on 2019-04-29 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('earnings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='soldsoftwares',
            name='developer',
        ),
    ]
