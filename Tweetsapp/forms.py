from django import forms
from .models import Tweet
max_length = 240


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > max_length:
            raise forms.ValidationError("this tweet is too long")
        return content
