from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'youremail@something'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))