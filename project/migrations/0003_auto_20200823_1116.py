# Generated by Django 3.1 on 2020-08-23 05:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20200822_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]