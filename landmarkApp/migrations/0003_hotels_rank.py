# Generated by Django 3.2 on 2021-09-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmarkApp', '0002_auto_20210924_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='rank',
            field=models.CharField(default='', max_length=10),
        ),
    ]
