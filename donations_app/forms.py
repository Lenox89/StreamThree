from django.forms import ModelForm
from django.core.exceptions import ValidationError
from models import Donations

class DonationForm(ModelForm):
    class Meta:
        model = Donations
        fields = ['card','code','month','year']