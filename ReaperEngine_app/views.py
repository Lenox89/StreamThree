# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
# from accounts_app.forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def donations(request):
    return render(request, "donations.html")


