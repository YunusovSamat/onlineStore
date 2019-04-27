from django import forms


class CatalogFilterForm(forms.Form):
    CHOICES = [
        ('price', 'по цене min'),
        ('-price', 'по цене max')
    ]
    sort = forms.ChoiceField(
        choices=CHOICES, widget=forms.RadioSelect, required=False,
    )
    sort.widget.attrs.update({'onChange': 'this.form.submit()'})
