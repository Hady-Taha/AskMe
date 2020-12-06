from django import forms
from django.contrib.auth.models import User
from ask.models import Message
from .models import Profile
# Create your forms here.
class Register(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password',)

    username=forms.CharField(
        max_length=25,
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'user name'}
            )
    )

    password=forms.CharField(
        min_length=9,
        required=True,
        widget=forms.PasswordInput(
            attrs={'class':'form-control','placeholder':'Password'}
            
            )
    )
    
    def clean(self):
        cd=self.cleaned_data
        if User.objects.filter(username=cd['username']):
            raise forms.ValidationError('username already exists')

    def usernamelenght(self):
        cd=self.changed_data
        if cd['username'] < 3:
            raise forms.ValidationError('username small')

        cd=self.changed_data
        if cd['username'] > 25:
            raise forms.ValidationError('username is too big')

    





class NewLogin(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password')
    
    username=forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class':'form-control','placeholder':'user name'}
            )
    )

    password=forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class':'form-control','placeholder':'Password'}
            
            )
    )

    


class NewMessage(forms.ModelForm):
    class Meta:
        model=Message
        fields=('messages',)
    
    messages=forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control','row':'3','placeholder':'massage'})
    )
    pass


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('profile_img','bio')
    pass