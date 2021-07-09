from django import forms

# FREE QUOTE FORM.


class FreeQuoteForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(max_length=200)
