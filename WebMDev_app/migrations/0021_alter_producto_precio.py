# Generated by Django 4.1.7 on 2023-03-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMDev_app', '0020_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]