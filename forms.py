from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime 


from evaluations.models import Evaluation

class BountyBoardForm(forms.ModelForm):
    class Meta:
        model = BountyBoard
        fields = '__all__'
        