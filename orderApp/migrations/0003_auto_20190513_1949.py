# Generated by Django 2.1.7 on 2019-05-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderApp', '0002_auto_20190513_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productorder',
            name='price',
        ),
        migrations.AlterField(
            model_name='productorder',
            name='size',
            field=models.IntegerField(),
        ),
    ]