# Generated by Django 2.1.7 on 2019-05-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productorder',
            name='update',
        ),
        migrations.AddField(
            model_name='productorder',
            name='price',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]