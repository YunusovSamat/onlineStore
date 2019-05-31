from django import forms


class OrderAddProductForm(forms.Form):
    count_id = forms.IntegerField()


class OrderForUserForm(forms.Form):
    address = forms.CharField()
    phone = forms.IntegerField()


class OrderForAnonymUserFrom(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    phone = forms.IntegerField()
