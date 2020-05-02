from django import forms
from django.forms import ModelForm


from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from .models import demo,UserDetails,User,payments
#SEND MAIL

class Demo(ModelForm):
    class Meta:
        model = demo
        fields = ['business']




#Register
class AddUserForm(ModelForm):
    class Meta:
        model = UserDetails
        fields = ['user_phone', 'user_gender']



class UserLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(render_value=False)
    )

    def clean(self):
        user = self.authenticate_via_email()
        if not user:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        else:
            self.user = user
        return self.cleaned_data

    def authenticate_user(self):
        return authenticate(
            username=self.user.username,
            password=self.cleaned_data['password'])

    def authenticate_via_email(self):
        """
            Authenticate user using email.
            Returns user object if authenticated else None
        """
        email = self.cleaned_data['email']
        if email:
            try:
                user = User.objects.get(email__iexact=email)
                if user.check_password(self.cleaned_data['password']):
                    return user
            except ObjectDoesNotExist:
                raise forms.ValidationError("Sorry, that login was invalid. Please try again.")

        return user

