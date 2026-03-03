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