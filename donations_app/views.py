# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from accounts_app.forms import UserRegistrationForm, UserLoginForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from ReaperEngine_prj.settings import AUTH_USER_MODEL
from ReaperEngine_prj.settings import STRIPE_SECRET
from forms import DonationForm
import datetime
import stripe

# Create your views here.
stripe.api_key = STRIPE_SECRET


def donations(request):
    if request.method == 'POST':
        print request.POST
        stripe.Charge.create(
            amount=2000,
            currency="usd",
            source="tok_visa",  # obtained with Stripe.js
            description="Donation for ReaperEngine"
        )
    return render(request,'donations.html', {'form':DonationForm()})