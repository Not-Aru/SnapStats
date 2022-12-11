create index IX_team_ids2 on app_games (home_team_id, away_team_id);

create index IX_stad_ids3 on app_stadium (stadium_id, stadium_name);

create index IX_broadcast_ids2 on app_broadcast_networks (id, broadcast_company);

create index IX_teamplayer2 on app_players (player_id, team_id);

create index IX_teamcollege2 on app_players (player_id, college);

create index IX_team2 on app_teams (team_id, team_name);