# Generated by Django 4.2.15 on 2024-08-10 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.TextField(verbose_name='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
