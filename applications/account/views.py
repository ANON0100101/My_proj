from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from applications.account.serializers import *

User = get_user_model()


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            'Вы успешно зарегистрировались. Вам отправлено письмо на почту с активацией',
            status=201
        )


class ActivationAPIView(APIView):

    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save(update_fields=['is_active', 'activation_code'])
        return Response('Успешно', status=200)


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializers = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializers.is_valid(raise_exception=True)
        serializers.set_new_password()
        return Response('Пароль изменен')


class ForgotPasswordAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('Вам отправлено на эту почту письмо с кодом для восстановления пароля', status=200)


class ForgotPasswordConfirmAPIView(APIView):
    def post(self, request):
        serializer = ForgotPasswordConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Пароль успешно обновлен', status=200)


@api_view(['GET'])
def send_mail_view(request):
    from applications.account.tasks import send_test_message
    send_test_message.delay()
    return Response('отправлено!')

