# Generated by Django 3.1 on 2020-08-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20200827_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=models.TextField(),
        ),
    ]
