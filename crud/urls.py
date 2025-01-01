from django.urls import path
from .views import *

urlpatterns = [
    path("create", create_view, name="create-view"),
    path("update/<int:id>", update_view, name="update-view"),
    path("retrieve", retrieve_view, name="retrieve-view"),
    path("detail/<int:id>", detail_view, name="detail-view"),
    path("delete/<int:id>", delete_view, name="delete-view"),


    path("home", home, name="home"),
]
