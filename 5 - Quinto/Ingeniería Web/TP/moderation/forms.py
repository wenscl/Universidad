from django import forms
from .models import ban_type

class BanForm(forms.Form):
    content_id = forms.IntegerField(widget=forms.HiddenInput())
    type_ban = forms.ChoiceField(
        label='Baneo',
        choices=[(ban_type[x], x[1]) for x in sorted(ban_type.keys())],
        widget=forms.Select(attrs={'class': 'form-control'}),
    )