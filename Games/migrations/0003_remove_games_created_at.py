# Generated by Django 3.2.11 on 2022-01-16 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0002_alter_games_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='created_at',
        ),
    ]