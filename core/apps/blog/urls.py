from django.urls import path
from core.apps.blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogPageView.as_view(), name='blog_page'),
]
