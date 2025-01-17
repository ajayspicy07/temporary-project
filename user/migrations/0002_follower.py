# Generated by Django 3.1 on 2020-08-20 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('from_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='user.profile')),
                ('to_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='user.profile')),
            ],
        ),
    ]
