
from django import forms
from .models import Empolyee


class EmpolyeeCreateForm(forms.ModelForm):

    class Meta:
        model = Empolyee
        fields = '__all__'


class EmpolyeeUpdateForm(forms.ModelForm):

    class Meta:
        model = Empolyee
        fields = '__all__'
