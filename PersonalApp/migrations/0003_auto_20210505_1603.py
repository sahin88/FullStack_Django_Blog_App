# Generated by Django 3.2.1 on 2021-05-05 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalApp', '0002_auto_20210505_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about_model',
            name='image_7',
        ),
        migrations.RemoveField(
            model_name='about_model',
            name='image_8',
        ),
    ]
