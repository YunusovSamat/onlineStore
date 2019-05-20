# Generated by Django 2.1.7 on 2019-05-18 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogApp', '0002_auto_20190518_2101'),
        ('productApp', '0005_auto_20190518_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductJoinColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_color_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_join_color', to='productApp.ColorProduct')),
                ('fk_subcatalog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_join_color', to='catalogApp.Subcatalog')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='fk_color_product',
        ),
    ]