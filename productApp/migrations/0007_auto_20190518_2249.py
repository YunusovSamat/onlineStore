# Generated by Django 2.1.7 on 2019-05-18 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0006_auto_20190518_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productjoincolor',
            name='fk_subcatalog',
        ),
        migrations.AddField(
            model_name='productjoincolor',
            name='fk_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_join_color', to='productApp.Product'),
        ),
    ]
