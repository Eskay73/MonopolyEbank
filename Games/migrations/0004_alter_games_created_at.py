# Generated by Django 3.2.11 on 2022-01-14 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0003_alter_games_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 15, 1, 13, 4, 974571)),
        ),
    ]