# Generated by Django 4.1.5 on 2023-03-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMDev_app', '0009_user_usercreationform_alter_producto_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mensaje',
            field=models.CharField(default='', max_length=40),
        ),
    ]