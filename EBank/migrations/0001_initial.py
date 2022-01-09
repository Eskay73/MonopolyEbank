# Generated by Django 3.2.11 on 2022-01-09 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerName', models.TextField()),
                ('money', models.PositiveIntegerField()),
                ('getOutOFJail', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='deed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyName', models.TextField()),
                ('cost', models.PositiveIntegerField()),
                ('rent', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=10)),
                ('houses', models.PositiveIntegerField()),
                ('hotels', models.PositiveIntegerField()),
                ('Owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='EBank.player')),
                ('currentPlayer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='current_player', to='EBank.player')),
            ],
        ),
    ]
