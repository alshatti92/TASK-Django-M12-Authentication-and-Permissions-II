from socket import fromshare
from django import froms
from django.contrib.auth import get_user_model


user = get_user_model()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ["username", "password"]

        widgets = {
            "password": forms.PasswordInput(),
        }
