from django import forms 
from crud_with_postgresql.models import EmpModel

class Empforms(forms.ModelForm):
    class Meta:
        model=EmpModel
        fields='__all__'
    