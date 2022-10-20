from enum import unique
from django.db import models

# Create your models here.

class Teams(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.TextField()
    stadium = models.TextField()
    division = models.TextField()

class Players(models.Model):
    player_id = models.IntegerField(unique)
    player_name = models.TextField()
    position = models.TextField()
    p_weight = models.FloatField()
    p_height = models.FloatField()
    team_id = models.ForeignKey("Teams", on_delete=models.SET_NULL, null=True)
    college = models.TextField()