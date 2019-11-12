from allauth.account.forms import SignupForm
from django import forms

from .choices import GENDERS, YEARS, MONTHS


class MyCustomSignupForm(SignupForm):
    month = forms.ChoiceField(required=True, choices=MONTHS, widget=forms.Select)
    year = forms.ChoiceField(required=True, choices=YEARS, widget=forms.Select)
    gender = forms.ChoiceField(choices=GENDERS, widget=forms.Select, required=True)

    def save(self, request):

        user = super(MyCustomSignupForm, self).save(request)

        user.profile.gender = self.cleaned_data['gender']
        user.profile.month = self.cleaned_data['month']
        user.profile.year = self.cleaned_data['year']
        user.save()

        # You must return the original result.
        return user