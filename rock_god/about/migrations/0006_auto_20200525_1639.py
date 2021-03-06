# Generated by Django 3.0.6 on 2020-05-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20200525_1242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dealer',
            old_name='four_hour_cost',
            new_name='cocaine_cost',
        ),
        migrations.RenameField(
            model_name='dealer',
            old_name='one_hour_cost',
            new_name='cocaine_tension_decrease',
        ),
        migrations.RenameField(
            model_name='dealer',
            old_name='three_hour_cost',
            new_name='heroine_cost',
        ),
        migrations.RenameField(
            model_name='dealer',
            old_name='two_hour_cost',
            new_name='heroine_tension_decrease',
        ),
        migrations.RenameField(
            model_name='fastfood',
            old_name='four_hour_cost',
            new_name='cost_one_person',
        ),
        migrations.RenameField(
            model_name='fastfood',
            old_name='one_hour_cost',
            new_name='tension_decrease_four_hour',
        ),
        migrations.RenameField(
            model_name='fastfood',
            old_name='three_hour_cost',
            new_name='tension_decrease_one_hour',
        ),
        migrations.RenameField(
            model_name='fastfood',
            old_name='two_hour_cost',
            new_name='tension_decrease_three_hour',
        ),
        migrations.RenameField(
            model_name='hospital',
            old_name='cost',
            new_name='cost_one_person',
        ),
        migrations.RenameField(
            model_name='pub',
            old_name='four_hour_cost',
            new_name='cost_one_person',
        ),
        migrations.RenameField(
            model_name='pub',
            old_name='one_hour_cost',
            new_name='tension_decrease_four_hour',
        ),
        migrations.RenameField(
            model_name='pub',
            old_name='three_hour_cost',
            new_name='tension_decrease_one_hour',
        ),
        migrations.RenameField(
            model_name='pub',
            old_name='two_hour_cost',
            new_name='tension_decrease_three_hour',
        ),
        migrations.RenameField(
            model_name='strip',
            old_name='four_hour_cost',
            new_name='cost_one_person',
        ),
        migrations.RenameField(
            model_name='strip',
            old_name='one_hour_cost',
            new_name='tension_decrease_four_hour',
        ),
        migrations.RenameField(
            model_name='strip',
            old_name='three_hour_cost',
            new_name='tension_decrease_one_hour',
        ),
        migrations.RenameField(
            model_name='strip',
            old_name='two_hour_cost',
            new_name='tension_decrease_three_hour',
        ),
        migrations.AddField(
            model_name='dealer',
            name='weed_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dealer',
            name='weed_tension_decrease',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fastfood',
            name='tension_decrease_two_hour',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pub',
            name='tension_decrease_two_hour',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='strip',
            name='tension_decrease_two_hour',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
