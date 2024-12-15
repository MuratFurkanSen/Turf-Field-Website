from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from .forms import TeamCreationForm
from .models import Team
from user.models import TeamInvite


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
        send_team_invite_to_user(team_id, user_id)
        return redirect(f"/team/{team_id}")
    elif op == "remove":
        if user_id == team.captain.id:
            print('You can\'t remove yourself')
            return redirect(f"/team/{team_id}")
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
    selected_team = Team.objects.get(id=team_id)
    if request.user not in selected_team.members.all():
        return HttpResponseForbidden("You are not a member of this team")
    context = {'id': team_id, 'team': selected_team}
    return render(request, 'team.html', context)

def send_team_invite_to_user(team_id, user_id):
    selected_team = Team.objects.get(id=team_id)
    selected_user = User.objects.get(id=user_id)
    invite = TeamInvite(team=selected_team, user=selected_user)
    invite.save()
    return redirect(f"/team/{team_id}")