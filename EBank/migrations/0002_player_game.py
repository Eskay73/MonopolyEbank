# Generated by Django 3.2.11 on 2022-01-09 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Games', '0002_alter_games_created_at'),
        ('EBank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='game',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to='Games.games'),
        ),
    ]
