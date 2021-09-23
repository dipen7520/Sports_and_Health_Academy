from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('login', views.login,name='login'),
    path('register',views.register,name="register"),
    path('otpcheck', views.otpcheck, name='otpcheck'),
    path('forget_password', views.forget_password, name='forget_password'),
    path('forget_password_email_form', views.forget_password_email_form, name='forget_password_email_form'),
    path('forget_password_form', views.forget_password_form, name='forget_password_form'),
    path('logout',views.logout,name="logout"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('service',views.service,name="service"),
    path('plan',views.plan,name="plan"),
    path('history',views.history,name="history"),
    path('contact',views.contact,name="contact"),
    path('trainer',views.trainer,name="trainer"),
    path('profile',views.profile,name="profile"),
    path('reg',views.reg,name="reg"),
]