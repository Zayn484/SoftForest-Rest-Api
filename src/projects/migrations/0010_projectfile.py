# Generated by Django 2.1.7 on 2019-04-19 06:58

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\ZAYN\\WebDev\\SoftForest\\backend\\src\\static_cdn\\protected_media'), upload_to=projects.models.upload_project_file_loc)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]
