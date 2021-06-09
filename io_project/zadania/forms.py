from django import forms

class OdpForm(forms.Form):
    odp = forms.CharField(label='Twoja odpowiedź', max_length=100)

class EmptyForm(forms.Form):
    pass

class LoginForm():
    pass

class RegisterForm():
    pass