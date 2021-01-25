from django import forms
from App_Quiz.models import QuizName, QuizQuestion, QuizTaker




class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['quiz_name', 'question', 'option1','option2','option3','option4','answer',]
