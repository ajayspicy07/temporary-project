# Generated by Django 3.1 on 2020-08-28 04:28

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20200828_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
