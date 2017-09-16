
from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = "like_app"
urlpatterns = [
    url(r"^",views.add_like_to_item, name="add_like")
]