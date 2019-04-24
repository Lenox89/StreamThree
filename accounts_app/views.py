# -*- coding: utf-8 -*-
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts_app.forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.core import serializers
from support_app.models import Ticket, Comment, VoteTracker
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            
            try:
                form.save()
                user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password1'))
            except IntegrityError:
                print "This email is already in use. Try logging in instead."
                messages.error(request, "This email is already in use. Try logging in instead.")
                return redirect(reverse('register'))

            if user:
                messages.success(request, "You have successfully registered")
                auth.login(request, user)
                return redirect(reverse('profile'))

            else:
                messages.error(request, "unable to log you in at this time!")

        else:
            form = UserRegistrationForm()

        args = {'form': form}
        args.update(csrf(request))

        return render(request, 'register.html', args)

    form = UserRegistrationForm();
    args = {'form': form};
    return render(request, 'register.html', args)

@login_required(login_url='/login/')
def profile(request):
    tickets = Ticket.objects.filter(user=request.user)
    comments = Comment.objects.filter(user=request.user)
    return render(request, 'profile.html',{"tickets": tickets, "comments": comments})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                     password=request.POST.get('password'))
            print user

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form':form}
    args.update(csrf(request))
    return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('home'))

def data(request):
    data = serializers.serialize("json", Ticket.objects.all())
    return HttpResponse(data)
