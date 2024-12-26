from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("current_datetime", current_datetime, name="current_datetime"),
    path("get_student", get_students, name="get_students"),
    path("tempview", TempView.as_view(), name="tempview"),
    path("rd/<int:pk>", Rd.as_view(), name='redirect-task'),
    path("student/<int:pk>", SingleStudent.as_view(), name="single-student"),
    path("rdt", RedirectView.as_view(url="http://youtube.com/veryacademy"), name="go-to-very"),
    path("get_name/<str:name>", get_name, name= "get-name"),
        # path("tempview", TemplateView.as_view(template_name = "", extra_context = {"": ""}), name="tempview")

#Passing Extra Options to View Function
    path("extra_option", extra_option,  {"extra_option": "this is an extra option" },name="extra-option")

]
