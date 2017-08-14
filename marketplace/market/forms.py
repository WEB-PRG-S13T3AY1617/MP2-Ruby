from django import forms
from django.forms import widgets, ModelChoiceField
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.models import User
from .models import Post, Offer, Profile


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        
        if username and password:
            user = authenticate(username = username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password") 
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
        return super(UserLoginForm, self).clean(*args, **kwargs)
    
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
        ]
        widgets = {
            'username': forms.TextInput(attrs={'required': True, 'placeholder':'Enter a username'}),
            'password': forms.PasswordInput(attrs={'required': True, 'placeholder':'Enter a password'}),
            'first_name': forms.TextInput(attrs={'required': True, 'placeholder':'Enter first name'}),
            'last_name': forms.TextInput(attrs={'required': True,'placeholder':'Enter last name'}),
        }
        
        labels = {
            'username': 'Username',
            'password': 'Password',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        coursename = forms.CharField(required=False)
        exclude = [
            'user',
        ]
        fields = [
            'tb_img',
            'itemname',
            'quantity',
            'condition',
            'tag',
            'posttypes',
            'coursename',
        ]
        
        widgets = {
            'itemname': forms.TextInput(attrs={'required': True, 'placeholder':'Enter item name'}),
            'condition': forms.TextInput(attrs={'required': True, 'placeholder': 'Enter condition of item'}),
            'tag': forms.TextInput(attrs={'required': True, 'placeholder': 'Enter tag for item'}),
            #'posttypes': forms.TextInput(attrs={'required': True}),
            'coursename': forms.TextInput(attrs={'required': False, 'placeholder': 'Enter coursename'}),
            
        }
        
        labels = {
            'tb_img':'Image',
            'itemname':'Name of Item',
            'quantity':'Quantity',
            'condition':'Condition of Item',
            'tag':'Item Tag',
            'posttypes':'What is the item for?',
            'coursename':'Course Name',
        }
        
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [
            'user',
        ]
        fields = [
            'usertypes',
            'Degree_Program_or_Office',
        ]
        widgets = {
            #'usertypes': forms.TextInput(attrs={'required': True}),
            'Degree_Program_or_Office': forms.TextInput(attrs={'required': True, 'placeholder':'Degree Program/Office'}),
        }
        
        labels = {
            'usertypes':'Occupation',
            'Degree_Program_or_Office':'Degree Program/Office',
        }