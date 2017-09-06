from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^logout$', views.logout, name = "logout"),
    url(r'^add$', views.add, name = "add"),
    url(r'^create_cat$', views.create_cat, name = "create_cat"),
    url(r'^(?P<user_id>\d+)/(?P<cat_id>\d+)$', views.add_like, name = "add_like"),
    url(r'^show/(?P<cat_id>\d+)$', views.show, name = "show"),
    url(r'^delete/(?P<cat_id>\d+)$', views.delete, name = "delete"),
    url(r'^update/(?P<cat_id>\d+)$', views.update, name = "update"),
    url(r'^edit$', views.edit, name = "edit"),
]