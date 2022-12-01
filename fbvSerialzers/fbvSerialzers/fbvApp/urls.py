from django.urls import path
from . import views
urlpatterns = [
    path('student/',views.student_list),
    path('student/<int:pk>',views.student_detail)
]