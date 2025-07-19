from django.urls import path
from .views import BookApiView,UniversalApiView,CreateApiView

urlpatterns = [
    path('', BookApiView.as_view()),
    path('<int:pk>/',UniversalApiView.as_view()),
    path('create/',CreateApiView.as_view()),
]