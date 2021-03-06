# Generated by Django 3.2 on 2021-09-29 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landmarkApp', '0008_auto_20210929_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('dwdw', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='hotels',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='landmarks',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
