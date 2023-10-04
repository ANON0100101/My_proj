from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from spam.models import Contact
from spam.serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated


class ContactAPIView(mixins.CreateModelMixin,mixins.DestroyModelMixin, GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(email=self.request.user.email)


