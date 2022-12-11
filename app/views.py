from functools import reduce
from tokenize import Single
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django_tables2 import SingleTableView
from django.http import HttpResponseRedirect
from django.db import connection
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from app.models import *
from app.tables import *
from app.forms import CreateUserForm
from django.db import transaction

# Create your views here.

class TeamsListView(SingleTableView):
    model = Teams
    table_class = TeamsTable
    template_name = 'app/teams.html'


class StadiumsListView(SingleTableView):
    model = Stadium
    table_class = StadiumsTable
    template_name = 'app/stadium.html'


class PlayersListView(SingleTableView):
    model = Players
    table_class = PlayersTable
    template_name = 'app/players.html'


class GamesListView(SingleTableView):
    model = Games
    table_class = GamesTable
    template_name = 'app/games.html'


class BroadcastNetworksListView(SingleTableView):
    model = Broadcast_Networks
    table_class = BroadcastNetworksTable
    template_name = 'app/broadcast_networks.html'


@login_required(login_url='loginPage')
def AlterTable(request):
    if request.method == 'POST':
        if request.POST.get('stadium_id') and request.POST.get('stadium_name') and request.POST.get('stadium_capacity'):
            stadium = Stadium()
            stadium.stadium_id = request.POST.get('stadium_id')
            stadium.stadium_name = request.POST.get('stadium_name')
            stadium.capacity = request.POST.get('stadium_capacity')
            stadium.save()

            return render(request, 'app/thanks.html')
        if request.POST.get('team_id') and request.POST.get('stadium_id') and request.POST.get(
                'team_name') and request.POST.get('division'):
            teams = Teams()
            teams.team_id = request.POST.get('team_id')
            teams.stadium_id = Stadium.objects.get(pk=request.POST.get('stadium_id'))
            teams.team_name = request.POST.get('team_name')
            teams.division = request.POST.get('division')
            teams.save()

            return render(request, 'app/thanks.html')
        if request.POST.get('player_id') and request.POST.get('player_name') and request.POST.get(
                'position') and request.POST.get('player_team_id') and request.POST.get(
                'player_age') and request.POST.get('player_years_on_team') and request.POST.get(
                'player_games_started') and request.POST.get('player_college'):
            player = Players()
            player.player_id = request.POST.get('player_id')
            player.player_name = request.POST.get('player_name')
            player.position = request.POST.get('position')
            player.team_id = Teams.objects.get(pk=request.POST.get('player_team_id'))
            player.player_age = request.POST.get('player_age')
            player.years_on_team = request.POST.get('player_years_on_team')
            player.games_started = request.POST.get('player_games_started')
            player.college = request.POST.get('player_college')
            player.save()

            return render(request, 'app/thanks.html')
        if request.POST.get('bn_company') and request.POST.get('bn_game_id'):
            bn = Broadcast_Networks()
            bn.broadcast_company = request.POST.get('bn_company')
            bn.game_id = Games.objects.get(pk=request.POST.get('bn_game_id'))
            bn.save()

            return render(request, 'app/thanks.html')
        if request.POST.get('games_game_id') and request.POST.get('games_home_team_id') and request.POST.get(
                'games_away_team_id') and request.POST.get('games_home_team_points') and request.POST.get(
                'games_away_team_points'):
            games = Games()
            games.game_id = request.POST.get('games_game_id')
            games.home_team_id = Teams.objects.get(pk=request.POST.get('games_home_team_id'))
            games.away_team_id.capacity = Teams.objects.get(pk=request.POST.get('games_away_team_id'))
            games.home_team_points = request.POST.get('games_home_team_points')
            games.away_team_points = request.POST.get('games_away_team_points')
            games.save()

            return render(request, 'app/thanks.html')

        # -----------------------------------------------------------------------------------------------------------------------------------------------

        if request.POST.get('stadium_update_set') and request.POST.get('stadium_update_where'):
            sql_query = "UPDATE app_stadium SET " + request.POST.get(
                'stadium_update_set') + " WHERE " + request.POST.get('stadium_update_where')
            cursor = connection.cursor()
            cursor.execute(sql_query)

            return render(request, 'app/thanks.html')
        if request.POST.get('team_update_set') and request.POST.get('team_update_where'):
            sql_query = "UPDATE app_teams SET " + request.POST.get('team_update_set') + " WHERE " + request.POST.get(
                'team_update_where')
            cursor = connection.cursor()
            cursor.execute(sql_query)

            return render(request, 'app/thanks.html')
        if request.POST.get('players_update_set') and request.POST.get('players_update_where'):
            sql_query = "UPDATE app_players SET " + request.POST.get(
                'players_update_set') + " WHERE " + request.POST.get('players_update_where')
            cursor = connection.cursor()
            cursor.execute(sql_query)

            return render(request, 'app/thanks.html')
        if request.POST.get('games_update_set') and request.POST.get('games_update_where'):
            sql_query = "UPDATE app_games SET " + request.POST.get('games_update_set') + " WHERE " + request.POST.get(
                'games_update_where')
            cursor = connection.cursor()
            cursor.execute(sql_query)

            return render(request, 'app/thanks.html')
        if request.POST.get('broadcast_networks_update_set') and request.POST.get('broadcast_networks_update_where'):
            sql_query = "UPDATE app_broadcast_networks SET " + request.POST.get(
                'broadcast_networks_update_set') + " WHERE " + request.POST.get('broadcast_networks_update_where')
            cursor = connection.cursor()
            cursor.execute(sql_query)

            return render(request, 'app/thanks.html')

        # -----------------------------------------------------------------------------------------------------------------------------------------------

        if request.POST.get('stadium_delete_where'):
            sql_query = "DELETE FROM app_stadium WHERE " + request.POST.get('stadium_delete_where')
            cursor = connection.cursor()
            cursor.execute(sql_query)

            return render(request, 'app/thanks.html')
        if request.POST.get('team_delete_where'):
            sql_query = "DELETE FROM app_teams WHERE " + request.POST.get('team_delete_where')
            cursor = connection.cursor()
            cursor.execute(sql_query)

            return render(request, 'app/thanks.html')
        if request.POST.get('players_delete_where'):
            sql_query = "DELETE FROM app_players WHERE " + request.POST.get('players_delete_where')
            cursor = connection.cursor()
            cursor.execute(sql_query)

            return render(request, 'app/thanks.html')
        if request.POST.get('games_delete_where'):
            sql_query = "DELETE FROM app_games WHERE " + request.POST.get('games_delete_where')
            cursor = connection.cursor()
            cursor.execute(sql_query)

            return render(request, 'app/thanks.html')
        if request.POST.get('broadcast_networks_delete_where'):
            sql_query = "DELETE FROM app_broadcast_networks WHERE " + request.POST.get(
                'broadcast_networks_delete_where')
            cursor = connection.cursor()
            cursor.execute(sql_query)

            return render(request, 'app/thanks.html')

    else:
        print(request)
        return render(request, 'app/alter_table.html')


@login_required(login_url='loginPage')
def CollegeReport(request):
    if request.method == 'POST':
        cursor = connection.cursor()

        player_id_string = ''
        player_position_string = ''
        player_age_string = ''
        player_yot_string = ''
        player_gs_string = ''
        players_team_string = ''
        players_where_team_clause = ''
        player_college_string = ''

        try:
            if request.POST.get('player_id'):
                player_id_string = ', p.' + request.POST.get('player_id')
            if (request.POST.get('position')):
                player_position_string = ', p.' + request.POST.get('position')
            if (request.POST.get('age')):
                player_age_string = ', p.' + request.POST.get('age')
            if (request.POST.get('years_on_team')):
                player_yot_string = ', p.' + request.POST.get('years_on_team')
            if (request.POST.get('games_started')):
                player_gs_string = ', p.' + request.POST.get('games_started')
            if (request.POST.get('college_select')):
                player_college_string = '\'' + request.POST.get('college_select') + '\''

            sql_query = "SELECT p.player_name, t.team_name" + player_id_string + player_position_string + player_age_string + player_yot_string + player_gs_string + " , p.college FROM app_players p, app_teams t WHERE p.college = " + player_college_string + ' AND p.team_id_id = t.team_id'
            print(sql_query)
            with transaction.atomic():
                cursor.execute('SET TRANSACTION ISOLATION LEVEL read committed')
                cursor.execute(sql_query)
                query = cursor.fetchall()
                cursor_desc = cursor.description
                desc_string = ' | '.join(desc[0] for desc in cursor_desc)
                field_names = [i[0] for i in cursor.description]

            return render(request, 'app/college_report.html', {'query': query, 'desc': desc_string, 'description':field_names})
        finally:
            cursor.close()
    else:
        return render(request, 'app/college_report.html')


@login_required(login_url='loginPage')
def ExperienceReport(request):
    if request.method == 'POST':
        cursor = connection.cursor()

        operator_string = ''

        try:
            if request.POST.get('operator_select'):
                operator_string = request.POST.get('operator_select')

            sql_query1 = ' Select winner, count(winner) from (Select * , case when home_team_points > away_team_points then "Home Team" when home_team_points < away_team_points then "Away Winner" else "Tie" end as winner from app_games) t1 Join (Select team_id_id, avg_age + avg_years_on_team + avg_games_started as home_sum from (Select team_id_id, avg(player_age) as avg_age, avg(years_on_team) as avg_years_on_team, avg(games_started) as avg_games_started from app_players group by team_id_id) t1a join (Select * from app_teams) t1b ON t1b.team_id = t1a.team_id_id) t2 ON t2.team_id_id = t1.home_team_id_id join (Select team_id_id, avg_age+avg_years_on_team+avg_games_started as away_sum from (Select app_players.team_id_id, avg(player_age) as avg_age, avg(years_on_team) as avg_years_on_team, avg(games_started) as avg_games_started from app_players group by app_players.team_id_id) t2a join (Select * from app_teams) t2b ON t2b.team_id = t2a.team_id_id) t3 ON t3.team_id_id = t1.away_team_id_id where home_sum '
            sql_query2 = operator_string + ' away_sum group by winner;'
            sql_query3 = sql_query1 + sql_query2;
            print(sql_query3)
            with transaction.atomic():
                cursor.execute('SET TRANSACTION ISOLATION LEVEL read committed')
                cursor.execute(sql_query3)
                query = cursor.fetchall()
                cursor_desc = cursor.description
                desc_string = ' | '.join(desc[0] for desc in cursor_desc)
                field_names = [i[0] for i in cursor.description]

            return render(request, 'app/experience_report.html', {'query': query, 'desc': desc_string, 'description':field_names})
        finally:
            cursor.close()
    else:
        return render(request, 'app/experience_report.html')


@login_required(login_url='loginPage')
def StadiumReport(request):
    if request.method == 'POST':
        cursor = connection.cursor()

        order_string = ''
        quantity_string = ''
        stadium_college_string = ''
        select_string = '*'

        try:
            # Get the values for the query parameters from the request
            if (request.POST.get('quantity')):
                quantity_string = ' limit ' + request.POST.get('quantity')
            if (request.POST.get('order')):
                order_string = request.POST.get('order')
            if (request.POST.get('stadium_select')):
                stadium_college_string = request.POST.get('stadium_select')
            if (request.POST.get('count')):
                select_string = ('count(*) as number_of_stadiums')

            # Use a with statement and the transaction.atomic decorator to ensure that
            # the database operations within the with block are executed as a single transaction
            with transaction.atomic():
                cursor.execute('SET TRANSACTION ISOLATION LEVEL read committed')



                sql_query = "select "+ select_string +" from app_stadium s where s.capacity " + stadium_college_string + order_string + quantity_string + ''

                print(sql_query)

                cursor.execute(sql_query)
                query = cursor.fetchall()
                cursor_desc = cursor.description
                desc_string = ' | '.join(desc[0] for desc in cursor_desc)
                field_names = [i[0] for i in cursor.description]

            # Return the result of the query
            return render(request, 'app/stadium_report.html', {'query': query, 'desc': desc_string, 'description':field_names})
        finally:
            cursor.close()
    else:
        return render(request, 'app/stadium_report.html')


@login_required(login_url='loginPage')
def index(request):
    return render(request, 'app/index.html')


@login_required(login_url='loginPage')
def reports(request):
    return render(request, 'app/reports.html')


@login_required(login_url='loginPage')
def collegeReport(request):
    return render(request, 'app/college_report.html')


@login_required(login_url='loginPage')
def thanks(request):
    return render(request, 'app/thanks.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or password is incorrect.')

    context = {}
    return render(request, 'app/login.html', context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('loginPage')
            else:
                messages.error(request,
                               'There was an error creating your account. Make sure that your password is not similar to the username and that it is at least 8 characters long.')

    context = {'form': form}
    return render(request, 'app/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginPage')


@login_required(login_url='loginPage')
def NetworksReport(request):
    if request.method == 'POST':
        cursor = connection.cursor()

        network_string = ''
        num_games_string = ''
        num_stadiums_string = ''
        num_points_string = ''

        try:
            if (request.POST.get('network_select')):
                network_string = '\'' + request.POST.get('network_select') + '\''
            if (request.POST.get('number_of_games')):
                num_games_string = ", COUNT(*) AS num_games_broadcasted"
            if (request.POST.get('number_of_stadiums')):
                num_stadiums_string = ', COUNT(DISTINCT t.stadium_id_id) AS num_stadiums'
            if (request.POST.get('number_of_points')):
                num_points_string = ', SUM(g.home_team_points + g.away_team_points) AS num_points'

            print("network_string: " + network_string);

            sql_query = "SELECT DISTINCT n.broadcast_company" \
                        + num_games_string \
                        + num_stadiums_string \
                        + num_points_string \
                        + " FROM app_broadcast_networks n" \
                        + " JOIN app_games g JOIN app_teams t JOIN app_stadium s ON n.game_id_id = g.game_id AND g.home_team_id_id = t.team_id AND t.stadium_id_id = s.stadium_id" \
                        + " WHERE n.broadcast_company = " + network_string

            print(sql_query)
            with transaction.atomic():
                cursor.execute('SET TRANSACTION ISOLATION LEVEL read committed')
                cursor.execute(sql_query)
                query = cursor.fetchall()
                cursor_desc = cursor.description
                desc_string = ' | '.join(desc[0] for desc in cursor_desc)
                field_names = [i[0] for i in cursor.description]

            return render(request, 'app/networks_report.html', {'query': query, 'desc': desc_string, 'description':field_names})
        finally:
            cursor.close()
    else:
        return render(request, 'app/networks_report.html')
