from django.urls import path
from account.api.views import (
    registration_view,
    account_properties_view,
    uppdate_account_view,
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = "account"

urlpatterns = [
    path('register', registration_view, name="register"),
    path('properties', account_properties_view, name="properties"),
    path('properties/update', uppdate_account_view, name="update"),
    path('login', obtain_auth_token, name="login"),
]