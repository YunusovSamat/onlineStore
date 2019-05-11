from django import forms


class OrderAddProductForm(forms.Form):
    count = forms.IntegerField()
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
