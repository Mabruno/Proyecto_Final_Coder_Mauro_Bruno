# Generated by Django 4.1.5 on 2023-03-08 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMDev_app', '0006_producto_imagen_producto_tamaño'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default=True, upload_to='static/WebMDev_app/assets/img'),
        ),
    ]