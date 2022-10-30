# Generated by Django 4.1.2 on 2022-10-30 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_games_game_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='games',
            name='game_date',
        ),
        migrations.RemoveField(
            model_name='players',
            name='p_height',
        ),
        migrations.RemoveField(
            model_name='players',
            name='p_weight',
        ),
        migrations.AddField(
            model_name='games',
            name='away_team_points',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='games',
            name='home_team_points',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='players',
            name='games_started',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='players',
            name='player_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='players',
            name='years_on_team',
            field=models.IntegerField(null=True),
        ),
    ]
