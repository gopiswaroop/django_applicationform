from django import forms
from regapp.models import student


class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'


class vendorform(forms.Form):
    name = forms.CharField(max_length=39)
    contact = forms.IntegerField()
    email = forms.EmailField(max_length=40)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


