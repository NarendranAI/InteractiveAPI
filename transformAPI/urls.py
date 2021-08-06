from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='Home'),
    path('TagNumber',views.tagNumber,name='TagNumber'),
    path('ReceivedDate',views.receivedDate,name='ReceivedDate'),
    path('ParentCompany',views.parentCompany,name='ParentCompany'),

]    