# Generated by Django 3.1 on 2020-08-30 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200830_0744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='previous_login',
        ),
    ]
