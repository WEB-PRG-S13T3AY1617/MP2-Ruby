from django import forms
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.models import User
from .models import Post, Offer, Profile
#superclass??

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
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
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
    def clean_photo(self):
        photo = self.cleaned_data.get('tb_img', False)
        if photo:
            fileType = photo.content_type
            if fileType in settings.VALID_IMAGE_FILETYPES: #png and jpeg
                return photo
        raise forms.ValidationError('FileType not supported: only upload jpegs and pngs.')
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [
            'user',
        ]
        fields = [
            'Degree_Program_or_Office',
            'usertypes'
        ]

        
class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude = [
            'post',
        ]
        fields = [
            'offertypes',
            'amount',
            'status',
        ]