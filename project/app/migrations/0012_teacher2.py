# Generated by Django 5.0.1 on 2024-01-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_select_tutor_teacher_remove_demorequest_tutor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username5', models.CharField(max_length=20)),
                ('email5', models.EmailField(max_length=254)),
                ('password5', models.CharField(max_length=20)),
                ('subject5', models.CharField(max_length=200)),
                ('availability5', models.CharField(max_length=200)),
                ('location5', models.CharField(max_length=100)),
                ('online_available5', models.BooleanField(default=False)),
                ('offline_available5', models.BooleanField(default=False)),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
        ),
    ]
