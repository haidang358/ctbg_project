# Generated by Django 4.1.2 on 2022-12-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0008_alter_luutrufile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='luutrufile',
            name='file',
            field=models.FileField(default=None, upload_to='clipboard'),
        ),
    ]
