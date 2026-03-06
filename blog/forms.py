from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Share your thoughts...',
                'class': 'form-control',
            })
        }
        labels = {
            'body': '',
        }

    def clean_body(self):
        body = self.cleaned_data.get('body', '')
        if not body.strip():
            raise forms.ValidationError('Comment cannot be empty.')
        if len(body) < 3:
            raise forms.ValidationError('Comment is too short.')
        return body

class StorySubmissionForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email address'})
    )
    destination = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Kyoto, Japan'})
    )
    pitch = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Tell us about your story — where did you go, what made it special?'
        })
    )
    photo_url = forms.URLField(
    required=True,
    widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'https://... (optional — a photo to accompany your story)'
    })
) 