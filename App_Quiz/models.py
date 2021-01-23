from django.db import models
from App_Login.models import User, user_type

# Create your models here.

class QuizName(models.Model):
    quiz_name = models.CharField(max_length=100)
    quiz_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_author')
    is_published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.quiz_name}'



class QuizQuestion(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    question_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_author')
    quiz_name = models.ForeignKey(QuizName, on_delete=models.CASCADE, related_name='name_of_quiz')
    def __str__(self):
        return f'{self.question}'



class QuizTaker(models.Model):
    score = models.FloatField(max_length=20)
    quiz_uniqe = models.ForeignKey(QuizName, on_delete=models.CASCADE, related_name='attended_quiz_name')
    quiz_attender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_taker')
    def __str__(self):
        return f'{self.quiz_attender}'
