from django.urls import path
from nsApp import views

urlpatterns = [
    path('author/',views.list_author.as_view()),
    path('author/<int:pk>',views.deatis_author.as_view()),
    path('book/',views.list_book.as_view()),
    path('book/<int:pk>',views.detail_book.as_view()),
]
