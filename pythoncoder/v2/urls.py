from django.urls import path
from pythoncoder.students.views import StudentView
from pythoncoder.v2.views import FormularioView,SearchView
from django.views.generic import TemplateView

app_name="v2"
urlpatterns=[
path("",TemplateView.as_view(template_name="v2/index.html"),name="v2"),
path("template/",TemplateView.as_view(template_name="v2/home.html"),name="template"),
path("aboutus/",TemplateView.as_view(template_name="v2/aboutus.html"),name="about-us"),
path("diigo",TemplateView.as_view(template_name="diigo/index.html"),name="diigo"),
path("student/",StudentView.as_view(),name="studentv2"),
path("formulario/",TemplateView.as_view(template_name="forms/index.html")),
path("search/", SearchView.as_view(),name="search")

]

#http://localhost:8000/v2/