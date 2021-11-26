from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form_input', 'placeholder':'Email',}), label='')
    tac = forms.BooleanField(initial=True, label='', widget=forms.CheckboxInput(attrs={'class':'register_checkbox'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'tac')
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form_input'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'form_input'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form_input'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'