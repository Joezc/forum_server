from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /item/0/
    url(r'^(?P<item_id>[0-9]+)/$', views.detail, name='detail'),
]
