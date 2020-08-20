from django import forms
from ghostpost.models import BoastRoast

class AddGhostpost(forms.ModelForm):
    class Meta:
        model = BoastRoast
        fields = ["choices", "user_input"]