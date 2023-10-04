from django.urls import path
from applications.account.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationAPIView.as_view()),
    path('change_password/', ChangePasswordAPIView.as_view()),
    path('forgot_password/', ForgotPasswordAPIView.as_view()),
    path('forgot_password_confirm/', ForgotPasswordConfirmAPIView.as_view()),
    path('test_celery/', send_mail_view)
]


