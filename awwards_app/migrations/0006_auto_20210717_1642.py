# Generated by Django 3.2 on 2021-07-17 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awwards_app', '0005_auto_20210717_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='average_rate',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='rate',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
