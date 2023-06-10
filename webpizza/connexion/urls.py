"""connexion URL Configuration"""

from django.urls import path, include
from django.contrib.auth import views as auth_views
from connexion import views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="connexion/login.html"), name='login'),

    # En mettant le template de login au lien de logout l'app porpose à l'utilisateur de se connecter tout de suiste apres ca deconnection
    #path("logout/", auth_views.LogoutView.as_view(template_name="connexion/logout.html"), name='logout'),
    path("logout/", auth_views.LogoutView.as_view(template_name="connexion/login.html"), name='logout'),

    path("register/", views.register, name='register'),

    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="connexion/password_reset.html", 
        email_template_name="connexion/password_reset_email.html"),name='password-reset'),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name='connexion/password_reset_confirm.html'), name = 'reset-password-confirm'),

    path("reset/done/", 
         auth_views.PasswordChangeDoneView.as_view(
             template_name='connexion/password_reset_done.html'), name='password_reset_done' ),

    
    path("reset/done/", 
         auth_views.PasswordChangeDoneView.as_view(
             template_name='connexion/password_complete.html'), name='password-reset-complete' ),

]
