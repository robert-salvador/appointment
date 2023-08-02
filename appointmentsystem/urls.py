from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name="register"),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name='password_reset_complete'),


    path('booking/', views.booking, name='booking'),
    path('booking-submit/', views.bookingSubmit, name='bookingSubmit'),
    path('staff-panel/', views.staffPanel, name='staffPanel'),
    path('delete_appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
] 