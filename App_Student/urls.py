from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = 'App_Student'

urlpatterns = [
    path('',views.student_home, name='student_home'),
    path('attempt_quiz',views.attempt_quiz, name='attempt_quiz'),
    path('quiz_running/<quiz_name>/<quiz_id>',views.quiz_running, name='quiz_running'),
    path('save_ans/',views.save_ans,name="save_ans"),
    path('result/',views.result,name="result"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
