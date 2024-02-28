from django import forms
from .models.winery import Winery


class WineryForm(forms.ModelForm):
    class Meta:
        model = Winery
        fields = ['name', 'image', 'region', 'location', 'description', 'grape_varieties', 'administrator_name',
                  'phone_number', 'email']


class WineryApprovalForm(forms.ModelForm):
    class Meta:
        model = Winery
        fields = ['approved']
        