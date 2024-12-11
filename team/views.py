from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from .forms import TeamCreationForm
from .models import Team


# Create your views here.
def create_team(request):
    if request.method == 'POST':
        form = TeamCreationForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.captain = request.user
            team.save()
            team.members.add(request.user)
            return redirect(f"/team/{team.id}")


def edit_team(request, team_id, op, user_id):
    team = Team.objects.get(id=team_id)
    if request.user != team.captain:
        return HttpResponseForbidden("You are not allowed to edit this team")
    if op == "add":
        user = User.objects.get(id=user_id)
        team.members.add(user)
        team.save()
        return redirect(f"/team/{team_id}")
    elif op == "remove":
        user = User.objects.get(id=user_id)
        team.members.remove(user)
        team.save()
        if len(team.members.all()) == 0:
            team.delete()
            return redirect(f"/")
        return redirect(f"/team/{team_id}")
    elif op == 'delete':
        team.delete()
        return redirect("/")


def team(request, team_id):
    team = Team.objects.get(id=team_id)
    if request.user not in team.members.all():
        return HttpResponseForbidden("You are not a member of this team")
    context = {'id': team_id, 'team': team}
    return render(request, 'team.html', context)
