# Generated by Django 3.1.2 on 2023-03-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20230309_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
    ]
