from django.forms import ModelForm
from .models import Ticket, Comment

class TicketForm(ModelForm):
  class Meta:
    model = Ticket
    fields = ['issue','type','description']

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']