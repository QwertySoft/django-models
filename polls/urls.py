from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='polls_index'),
    path('<int:poll_id>', views.detail, name='poll_detail'),
]
