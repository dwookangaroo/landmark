# Generated by Django 3.2 on 2021-09-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmarkApp', '0011_auto_20210929_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='landmarks',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]