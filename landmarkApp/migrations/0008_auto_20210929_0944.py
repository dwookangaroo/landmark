# Generated by Django 3.2 on 2021-09-29 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmarkApp', '0007_auto_20210929_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='represent',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='address',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='lat',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='lng',
            field=models.CharField(max_length=20),
        ),
    ]
