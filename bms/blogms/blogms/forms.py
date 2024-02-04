# forms.py
from django import forms
# from . import Feedback
from authentication.models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

        # button = ['Submit', 'Cancel']



