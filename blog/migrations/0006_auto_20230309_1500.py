# Generated by Django 3.1.2 on 2023-03-09 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_laptop_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes/productos'),
        ),
    ]
