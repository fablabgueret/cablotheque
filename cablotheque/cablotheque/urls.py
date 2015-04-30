# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('cable.urls', namespace="cable")),
    url(r'^admin/', include(admin.site.urls)),
]

admin.site.site_header = u"Cablothèque"

