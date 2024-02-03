from django.urls import path

from .views import user_login
from .views import logout

app_name = "users_accounts"
urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", logout, name="logout"),
]
