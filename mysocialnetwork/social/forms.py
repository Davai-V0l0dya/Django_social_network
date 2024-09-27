from django import forms
from django.contrib.auth.models import User

from .models import Post, Comment


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError("Пароли не совпадают.")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']