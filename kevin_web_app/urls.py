from django.urls import path
from . import views

urlpatterns=[
    path("",views.IndexView.as_view(),name="index"),
    path("api/v1/info",views.View_API.as_view())
]