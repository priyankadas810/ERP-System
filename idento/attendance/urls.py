from django.urls import path
from . import views



urlpatterns = [

    path('', views.index, name = 'index'),
    path('user_home/', views.user_home, name = 'user_home'),
    path('user_profile/', views.user_profile, name = 'user_profile'),
    path('user_info/', views.user_info, name = 'user_info'),
    path('user_otp/<id>', views.user_otp, name = 'user_otp'),
    path('userregistration/', views.userRegistration, name = 'userregister'),
    path('user_signin/', views.user_signin, name = 'user_signin'),
    path('qr_generator/', views.qr_generator, name = 'qr_generator'), 
    path('signout', views.signout, name = 'signout'),
    path('admin_home/', views.admin_home, name = 'admin_home'),
    path('adminregistration/', views.adminRegistration, name = 'adminregister'),
    path('admin_signin/', views.admin_signin, name = 'admin_signin'),
    path('admin_otp/<id>', views.admin_otp, name = 'admin_otp'),
    path('admin_profile/',views.admin_profile, name = 'admin_profile'),
    path('admin_info/',views.admin_info, name = 'admin_info'),
    path('membership_details/',views.membership_details, name = 'membership_details'),
    path('show_memberships_user/',views.show_memberships_user, name = 'show_memberships_user'),
    path('membership_upgrade/',views.membership_upgrade, name = 'membership_upgrade'),
    
]  