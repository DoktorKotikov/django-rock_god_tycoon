# Generated by Django 3.0.6 on 2020-06-01 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0010_auto_20200529_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='x',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gig',
            name='y',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
