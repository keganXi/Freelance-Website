from django import forms

# CONTACT US FORM.


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(max_length=200)
