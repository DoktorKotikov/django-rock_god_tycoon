# Generated by Django 3.0.6 on 2020-05-22 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20200522_1555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['fans_need']},
        ),
    ]
