from .models import UserUpdate
from django import forms


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserUpdate
        fields = ('Name', 'Mobile_Number', 'Mail_Address')