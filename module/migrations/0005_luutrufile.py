# Generated by Django 4.1.2 on 2022-12-01 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0004_alter_lathuoc_giaban_alter_lathuoc_madieutri_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='luuTruFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(default=None, upload_to='file')),
            ],
        ),
    ]
