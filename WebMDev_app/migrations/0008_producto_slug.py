# Generated by Django 4.1.5 on 2023-03-08 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMDev_app', '0007_alter_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]