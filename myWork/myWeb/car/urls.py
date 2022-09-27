from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('car/main/',views.car_view,name='car_view'),
    
]
urlpatterns += staticfiles_urlpatterns()