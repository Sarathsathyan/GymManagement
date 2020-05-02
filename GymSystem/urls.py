from django.conf.urls.static import static
from django.urls import path


from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('classes/',views.courses,name='classes'),
    path('single/<int:c_id>',views.single,name='single'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('demo/',views.Demos,name='demo'),
    path('features/',views.feature,name='features'),
    path('resources/',views.resources,name='resources'),
    path('register/',views.adduser,name='register'),
    path('payment/',views.Payment,name='payment'),
    path('handlerequest/',views.handlerequest,name='HandleRequest'),
    path('customer_courses/',views.customer_courses,name='customer_courses'),
    path('transformation/',views.Transformation,name='transformation'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),

    ]