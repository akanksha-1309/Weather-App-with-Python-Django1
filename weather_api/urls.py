from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("result", views.result, name="result"),
    path('fetch_weather/', views.fetch_weather, name='fetch_weather')
    # path('social_links', views.social_links),
]




