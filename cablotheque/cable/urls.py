from django.conf.urls import url

from .views import CableListView

urlpatterns = [
    url(r'^$', CableListView.as_view(), name='list'),
]