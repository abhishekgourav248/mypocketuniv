from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('email','password','username')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
