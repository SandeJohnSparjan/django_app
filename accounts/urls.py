from django.conf.urls import url
from django.urls import path,re_path
from django.contrib.auth.views import (
    LoginView ,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

# . means looks in folders for views file
from . import views
#for name space
#app_name= 'accounts'
#creating a list of URLS
urlpatterns = [
    path('',views.oldhome,name='accounts'),

    #rendering our login page than default page
    path('login/', LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('register/',views.register, name='register'),
    path('profile/',views.view_profile, name='view_profile'),
    path('profile/<int:pk>/',views.view_profile, name='view_profile_with_prime_key'),
    path('profile/edit/',views.edit_profile, name='edit_profile'),
    path('change-password/',views.change_password, name='change_password'),
    #?
    path('profile/password/', views.change_password, name='change_password'),

    #password resetting
    path('reset-password/', PasswordResetView.as_view(template_name='accounts/reset_password.html',success_url='/accounts/reset-password/done',email_template_name='accounts/reset_password_email.html'), name='reset_password'),
    #to send email
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    #to check if mail is being sent to valid user (by sendind ID and Token)
    path('reset-password/confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',success_url='/accounts/reset-password/complete/'), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete')

]