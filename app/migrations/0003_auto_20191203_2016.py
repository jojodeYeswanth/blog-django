# Generated by Django 3.0 on 2019-12-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191203_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpost',
            name='data',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='addpost',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
