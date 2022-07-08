from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='new')),
    path('new/', views.new, name='new'),
    path('preparing/', views.preparing, name='preparing'),
    path('completed/', views.completed, name='completed'),
    path('single/<int:id>/', views.single, name='single'),
]