# Generated by Django 2.1.7 on 2019-04-25 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modificationrequests', '0002_request_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(default='pending', max_length=50),
        ),
    ]
