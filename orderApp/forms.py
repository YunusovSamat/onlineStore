from django import forms


class OrderAddProductForm(forms.Form):
    count = forms.IntegerField()
    count_id = forms.IntegerField()


class OrderForUserForm(forms.Form):
    address = forms.CharField()
    comment = forms.CharField()


class OrderForAnonymUserFrom(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    comment = forms.CharField()
