# Generated by Django 2.1.7 on 2019-05-10 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('earnings', '0005_remove_soldsoftwares_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Sale Summary',
                'verbose_name_plural': 'Sales Summary',
                'proxy': True,
                'indexes': [],
            },
            bases=('earnings.soldsoftwares',),
        ),
    ]
