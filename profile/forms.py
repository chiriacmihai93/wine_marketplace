from django import forms
from .models.profile import Profile


class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        input_formats=['%d/%m/%Y'],  # Adaugă formate europene
        widget=forms.DateInput(attrs={'type': 'date'})  # Widget pentru câmpul de introducere a datei
    )

    class Meta:
        model = Profile
        fields = ['gender', 'date_of_birth', 'location', 'phone_number']

