from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^show/(?P<id>\w{0,50})/$', views.show),
    url(r'^create/', views.create, name='create'),
    url(r'^mark-completed/(?P<id>\w{0,50})/$', views.complete_todo, name='mark-completed'),
    url('delete-completed', views.delete_completed, name='delete-completed')
]
