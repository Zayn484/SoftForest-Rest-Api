# Generated by Django 2.1.7 on 2019-05-11 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20190419_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='on_sale',
            field=models.BooleanField(default=False),
        ),
    ]