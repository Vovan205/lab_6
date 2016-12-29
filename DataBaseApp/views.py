from django.shortcuts import render
from django.views import View

from DataBaseApp.models import Team


def main_page(request):
    return render(request, 'index.html')


class TeamView(View):
    def get(self, request):
        teams = Team.objects.all()
        return render(request, 'teams.html', {'teams': teams})