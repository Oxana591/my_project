from django.urls import path

from . import views

urlpatterns=[
    path('school/uch_find/',views.uch_find,name='uch_find'),
    path('school/uch_add/',views.uch_add,name='uch_add'),
]
