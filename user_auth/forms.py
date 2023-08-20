from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from .models import User, UserDetail
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(UserCreationForm):
    
    class Meta():
        model = User
        fields = ('email','document')
        labels = {
        "document": "Citizenship"}
        help_texts = {
            'password1': None,
            'password2': None,
        }

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("phone number is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    

class UserDetailForm(forms.ModelForm):
    class Meta():
        model = UserDetail
        exclude = ('user',)
        widgets = {
            'dob': forms.widgets.DateInput(attrs={'type': 'date'})
        }
       
