from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TodoListViews, TodoDetailViews

urlpatterns = [
    path('', TodoListViews.as_view()),
    path('<int:id>', TodoDetailViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
