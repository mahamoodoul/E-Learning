from django.contrib import admin
from App_Quiz.models import QuizName, QuizQuestion, QuizTaker
# Register your models here.


admin.site.register(QuizName)
admin.site.register(QuizQuestion)
admin.site.register(QuizTaker)
