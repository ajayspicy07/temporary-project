# Generated by Django 3.1 on 2020-08-19 13:09

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('dob', models.DateField()),
                ('user_mode', models.CharField(choices=[('STUDENT', 'student'), ('EDUCATOR', 'Proffesor/Teacher/Educator')], default='STUDENT', max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.college')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('img', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('description', models.TextField(blank=True, default='hai')),
                ('content_type', models.ForeignKey(limit_choices_to=models.Q(('model', 'user'), ('model', 'page'), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('college', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='user.college')),
                ('members', models.ManyToManyField(to='user.User')),
            ],
        ),
    ]
