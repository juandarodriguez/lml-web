from allauth.account.forms import SignupForm
from django import forms

from .widgets import MonthYearWidget
from .choices import GENDERS


class MyCustomSignupForm(SignupForm):
    birth_date = forms.DateField(required=True, widget=forms.SelectDateWidget)
    gender = forms.ChoiceField(choices=GENDERS, widget=forms.Select, required=True)

    def save(self, request):

        user = super(MyCustomSignupForm, self).save(request)

        #user.profile.gender = request.gender

        #user.profile.objects.save()

        # Add your own processing here.


        user.profile.gender = self.cleaned_data['gender'];
        user.save();

        # You must return the original result.
        return user