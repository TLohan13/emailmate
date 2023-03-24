from django.urls import path
from emailer_app import views

urlpatterns = [
    path('', views.emailer_view, name="emailer_view")
]
