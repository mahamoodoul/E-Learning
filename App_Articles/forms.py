from django import forms
from App_Articles.models import Comment, AnswerQuestion


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = AnswerQuestion
        fields = ('answer',)
