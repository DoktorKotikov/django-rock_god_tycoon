# Generated by Django 3.0.6 on 2020-06-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0012_auto_20200602_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='map',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
