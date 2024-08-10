from django import forms
from django.utils import timezone

from .models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.Textarea()
    date = timezone.now()

    class Meta:
        model = Comment
        fields = ['input']
