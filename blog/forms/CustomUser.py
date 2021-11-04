from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    '''Class  for customizing the user creation form'''
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    '''Class  for customizing the user change form'''
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)