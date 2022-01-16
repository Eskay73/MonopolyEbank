# Generated by Django 3.2.11 on 2022-01-16 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='games',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('gameName', models.CharField(max_length=50)),
                ('result', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 1, 16, 19, 37, 28, 534899))),
            ],
        ),
    ]
