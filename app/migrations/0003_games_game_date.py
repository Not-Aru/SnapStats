# Generated by Django 4.1.2 on 2022-10-29 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_stadium_remove_players_id_remove_teams_stadium_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='game_date',
            field=models.DateField(null=True),
        ),
    ]
