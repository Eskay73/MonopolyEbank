# Generated by Django 3.2.11 on 2022-01-16 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0004_games_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='gameName',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
