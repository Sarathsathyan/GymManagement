from django.conf.urls.static import static
from django.urls import path


from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('classes/',views.courses,name='classes'),
    path('single/<int:id>',views.single,name='single'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('demo/',views.Demos,name='demo'),
    path('features/',views.feature,name='features'),
    path('resources/',views.resources,name='resources'),

    ]