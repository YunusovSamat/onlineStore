from django import forms


class OrderAddProductForm(forms.Form):
    count = forms.IntegerField()
    count_id = forms.IntegerField()

