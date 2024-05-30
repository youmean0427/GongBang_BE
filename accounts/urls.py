# accounts/urls.py

from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    
)
from dj_rest_auth.views import (
    LoginView, LogoutView, UserDetailsView
)

app_name = 'accounts'
urlpatterns = [

    path('login/', LoginView.as_view(), name="rest_login"),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', include('dj_rest_auth.registration.urls')),
   
]