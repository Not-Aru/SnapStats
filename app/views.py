from tokenize import Single
from django.shortcuts import render
from django.views.generic import ListView
from django_tables2 import SingleTableView

from app.models import *
from app.tables import *

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

def index(request):
    return render(request, 'app/index.html')