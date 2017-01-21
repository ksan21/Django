from django.conf.urls import url, include
from .import views
# from django.contrib import admin

# urlpatterns = [
#     url(r'^', include('apps.timedisplay.urls'))

urlpatterns = [
      url(r'^$', views.index),
]
