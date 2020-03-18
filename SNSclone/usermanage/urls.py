from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='usermanage'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="usermanage/login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]
