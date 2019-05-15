# Generated by Django 2.1.7 on 2019-05-15 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orderApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='fk_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.PositiveIntegerField(),
        ),
    ]
