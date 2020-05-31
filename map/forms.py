from django import forms


class MapForm(forms.Form):
    post = forms.CharField()
