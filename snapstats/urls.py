"""snapstats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

import app.views as views
import snapstats.settings as settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teams/', views.TeamsListView.as_view()),
    path('stadiums/', views.StadiumsListView.as_view()),
    path('players/', views.PlayersListView.as_view()),
    path('games/', views.GamesListView.as_view()),
    path('broadcast-networks/', views.BroadcastNetworksListView.as_view()),
    path('alter_table/', views.AlterTable, name="alter"),
    path('thanks/', views.thanks, name="thanks"),
    path('', views.index, name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
