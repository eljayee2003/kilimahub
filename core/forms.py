from django import forms
from core.models import User

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    country = forms.CharField(max_length=2)
    referral_code = forms.CharField(required=False)

    def clean_referral_code(self):
        code = self.cleaned_data['referral_code']
        if code and not User.objects.filter(referral_count__gt=0).exists():
            raise forms.ValidationError("Invalid African referral code")
        return code
