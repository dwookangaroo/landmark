# Generated by Django 3.2 on 2021-09-29 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landmarkApp', '0003_hotels_rank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landmarks',
            name='address',
        ),
        migrations.RemoveField(
            model_name='landmarks',
            name='desc',
        ),
    ]