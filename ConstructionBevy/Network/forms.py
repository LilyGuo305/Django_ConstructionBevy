from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows' : 3,
            'placeholder' : 'Type here'
        })
    )

    class Meta:
        model = Post
        fields = ['body']


class ThreadForm(forms.Form):

    username = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': 1,
            'placeholder': 'username'
        })
    )

class MessageForm(forms.Form):

    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows' : 3,
            'placeholder' : 'Type here'
        })
    )