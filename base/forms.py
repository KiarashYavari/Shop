from django import forms
from django.core.exceptions import ValidationError

from base.models import Members


class SignUpForms(forms.ModelForm):
    agreement = forms.BooleanField(required=False)

    class Meta:
        model = Members
        fields = ('first_name', 'last_name', 'username', 'password', 'email')

    def clean_agreement(self):
        if not self.cleaned_data['agreement']:
            raise ValidationError("موافقت با قوانین الزامی است!")
