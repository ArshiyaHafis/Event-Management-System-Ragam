from django.forms import ModelForm
from .models import Event, UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password','phone')
        widgets = {
            'password': forms.PasswordInput(),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('event_name','event_link','event_date', 'event_time','event_image', 'event_descp','event_location')
    

class UserPForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_name', 'user_pic', 'user_no')