from django.contrib import admin
from django.urls import path, reverse_lazy
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.views import (
    PasswordResetView, PasswordResetConfirmView,
)
from django.contrib.auth import views as auth_views
from accounts.views import passwordResetRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('coffeecafes.urls')),
    path('accounts/', include('accounts.urls')),
    path('password/reset/',  PasswordResetView.as_view(), name="password_reset"),
    path('password/reset/confirm/<uid>/<token>/',passwordResetRedirect, 
     name='password_reset_confirm'),    
    path('password/reset/confirm/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)