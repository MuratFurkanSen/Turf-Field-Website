from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from .apps import TeamConfig
from .forms import TeamCreationForm, TeamUpdateForm
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


def edit_team(request, id,op):
    team = Team.objects.get(id=id)
    if request.user != team.captain:
        return HttpResponseForbidden("You are not allowed to edit this team")
    if request.method == 'POST':
        form = TeamUpdateForm(request.POST)
        if form.is_valid():
            team = Team.objects.get(id=id)
            if op == "add":
                user = User.objects.get(id=form.cleaned_data['id'])
                team.members.add(user)
                team.save()
            elif op == "remove":
                user = User.objects.get(id=form.cleaned_data['id'])
                team.members.remove(user)
                team.save()
            elif op == "delete":
                team.delete()
                return redirect("/")
            return redirect(f"/team/{id}")

def team(request, id):
    team = Team.objects.get(id=id)
    if request.user not in team.members.all():
        return HttpResponseForbidden("You are not a member of this team")
    create_form = TeamCreationForm()
    update_form = TeamUpdateForm()
    context = {'create_form': create_form, 'update_form': update_form, 'id': id, 'team': team}
    return render(request, 'team.html', context)
