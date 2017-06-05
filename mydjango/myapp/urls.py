from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index,name="index"),
    # url(r'^add/$', views.add,name="add"),
    # url(r'^create/$', views.create,name="create"),
    # url(r'^view/$', views.view,name="create"),
    # url(r'^edit/$', views.edit,name="create"),
    # url(r'^update/$', views.update,name="create"),
    # url(r'^delete/$', views.delete,name="delete"),
]