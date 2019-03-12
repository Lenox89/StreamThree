# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from forms import TicketForm, CommentForm
from models import Ticket, Comment, VoteTracker
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def support(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_id = request.user.id
            form.save()
            return redirect(reverse('support'))
    tickets = Ticket.objects.all()
    comments = Comment.objects.all()
    form = TicketForm()
    form2 = CommentForm()
    args = {'tickets': tickets, 'form': form, 'comments': comments, 'form2': form2}
    return render(request, "support.html", args)

@login_required(login_url='/login/')
def vote(request,id):
    vote = VoteTracker.objects.filter(ticket=id, user=request.user)

    if not vote:
        ticket = get_object_or_404(Ticket, pk=id)
        VoteTracker.objects.create(ticket=ticket, user=request.user)
        ticket.votes += 1
        ticket.save()
    return redirect(reverse('support'))

@login_required(login_url='/login/')
def comment(request,id):
    form = CommentForm(request.POST)
    form = form.save(commit=False)
    form.ticket_id = id
    form.user_id = request.user.id
    form.save()
    return redirect(reverse('support'))