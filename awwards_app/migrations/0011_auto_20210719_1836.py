# Generated by Django 3.2 on 2021-07-19 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwards_app', '0010_auto_20210718_2350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='aggregate_average_rate',
            new_name='average_rate',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='content_wise_average',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='design_wise_average',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='usability_wise_average',
        ),
    ]