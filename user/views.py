from django.contrib.auth import authenticate, login, logout, user_logged_in
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from user.forms import UserRegistrationForm, UserLoginForm
from user.models import TeamInvite, FriendInvite


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect('/')

    else:
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
    return redirect('/')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')

def user_invites(request):
    if request.user.is_authenticated:

        friend_invites = FriendInvite.objects.filter(recipient_user=request.user)
        team_invites = TeamInvite.objects.filter(user=request.user)
        print(friend_invites)
        print(team_invites)
        context = {'friend_invites': friend_invites, 'team_invites': team_invites}
        return render(request, 'invites.html', context)
    else:
        return redirect(request, '')


def send_friend_invite(request, recipient_id):
    if request.user.is_authenticated:
        sender = request.user
        recipient = User.objects.get(id=recipient_id)
        invite = FriendInvite(sender=sender, recipient=recipient)
        invite.save()
        return redirect('/')

def accept_friend_invite(request, invite_id):
    invite = FriendInvite.objects.get(id=invite_id)
    sender = invite.sender_user
    recipient = invite.recipient_user
    if recipient == request.user:
        sender.friends.add(recipient)
        recipient.friends.add(sender)
        sender.save()
        recipient.save()
        invite.delete()
        return redirect('/')
    else:
        return HttpResponseForbidden('Fuck Off')
def accept_team_invite(request, invite_id):
    invite = TeamInvite.objects.get(id=invite_id)
    team = invite.team
    user = invite.user
    if user == request.user:
        team.members.add(user)
        team.save()
        invite.delete()
        return redirect(f'/team/{team.id}')
    else:
        return HttpResponseForbidden('Fuck Off')

def decline_friend_invite(request, invite_id):
    invite = FriendInvite.objects.get(id=invite_id)
    recipient = invite.recipient_user
    if recipient == request.user:
        invite.delete()
        return redirect('/')
    else:
        return HttpResponseForbidden('Fuck Off')

def decline_team_invite(request, invite_id):
    invite = TeamInvite.objects.get(id=invite_id)
    user = invite.user
    if user == request.user:
        invite.delete()
        return redirect('/')
    else:
        return HttpResponseForbidden('Fuck Off')
