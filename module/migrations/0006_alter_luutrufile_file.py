# Generated by Django 4.1.2 on 2022-12-01 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0005_luutrufile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luutrufile',
            name='file',
            field=models.ImageField(default=None, upload_to='Users/haidang/Downloads/File'),
        ),
    ]
