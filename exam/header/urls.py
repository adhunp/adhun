from django.urls import path
from .import views
app_name='header'
urlpatterns=[
    # path('alogin',views.alogin,name='alogin'),
    path('vstudent',views.vstudent,name='vstudent'),
    path('de_students',views.de_students,name='de_students'),
    path('de_student/<int:student_id>',views.de_student,name='de_student'),
    path('edit/<int:student_id>',views.edit,name='edit'),

]