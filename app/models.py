from enum import unique
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Stadium(models.Model):
    stadium_id = models.IntegerField(primary_key=True)
    stadium_name = models.TextField()
    capacity = models.IntegerField(null=True)

class Teams(models.Model):
    team_id = models.IntegerField(primary_key=True)
    stadium_id = models.ForeignKey(Stadium, null=True, on_delete=models.CASCADE)
    team_name = models.TextField()
    division = models.TextField()

class Players(models.Model):
    player_id = models.IntegerField(primary_key=True)
    player_name = models.TextField()
    position = models.TextField()
    team_id = models.ForeignKey(Teams, on_delete=models.SET_NULL, null=True)
    player_age = models.IntegerField(null=True)
    years_on_team = models.IntegerField(null=True)
    games_started = models.IntegerField(null=True)
    college = models.TextField()

class Games(models.Model):
    game_id = models.IntegerField(primary_key=True)
    home_team_id = models.ForeignKey(Teams, related_name='related_home_team_id', verbose_name = 'Home Team ID', null=True, on_delete=models.CASCADE)
    away_team_id = models.ForeignKey(Teams, related_name='related_away_team_id', verbose_name='Away Team ID', null=True, on_delete=models.CASCADE)
    home_team_points = models.IntegerField(null=True)
    away_team_points = models.IntegerField(null=True)

class Broadcast_Networks(models.Model):
    broadcast_company = models.CharField(max_length=64, primary_key=True)
    game_id = models.ForeignKey(Games, null=True, on_delete=models.CASCADE)