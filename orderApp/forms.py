from django import forms


class OrderAddProductForm(forms.Form):
    product_id = forms.IntegerField()
    count = forms.IntegerField()
    size = forms.IntegerField()

