# Generated by Django 2.1.5 on 2019-08-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='staff',
            name='title_en',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='staff',
            name='title_hu',
            field=models.CharField(max_length=100),
        ),
    ]
