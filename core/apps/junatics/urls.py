from django.urls import path
from core.apps.junatics import views

app_name = 'junatics'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
]
