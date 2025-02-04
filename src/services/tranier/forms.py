from django import forms
from .models import Trainer

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = [ "user","name", "specialization", "experience", "phone_number"]
