from django.urls import path
from django.views.generic import TemplateView

app_name = 'articleapp'

urlpatterns = [

    path('list/', TemplateView.as_view(templete_name='articleapp/list.html'), name='list')


]