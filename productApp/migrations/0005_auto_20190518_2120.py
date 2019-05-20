# Generated by Django 2.1.7 on 2019-05-18 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0004_auto_20190518_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colorproduct',
            name='fk_product',
        ),
        migrations.AddField(
            model_name='product',
            name='fk_color_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='productApp.ColorProduct'),
        ),
    ]