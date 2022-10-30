import django_tables2 as tables
import app.models as models

class TeamsTable(tables.Table):
    class Meta:
        model = models.Teams
        template_name = "django_tables2/bootstrap.html"
        fields = ("team_id", "stadium_id_id", "team_name", "division")

class StadiumsTable(tables.Table):
    class Meta: 
        model = models.Stadium
        template_name = "django_tables2/bootstrap.html"
        fields = ("stadium_id", "stadium_name", "capacity")

class PlayersTable(tables.Table):
    class Meta: 
        model = models.Players
        template_name = "django_tables2/bootstrap.html"
        fields = ("player_id", "player_name", "position", "team_id_id", "player_age", "years_on_team", "games_started", "college")
    
class BroadcastNetworksTable(tables.Table):
    class Meta: 
        model = models.Broadcast_Networks
        template_name = "django_tables2/bootstrap.html"
        fields = ("broadcast_company", "game_id_id")

class GamesTable(tables.Table):
    class Meta:
        model = models.Games
        template_name = "django_tables2/bootstrap.html"
        fields = ("game_id", "home_team_id_id", "away_team_id_id", "home_team_points", "away_team_points")