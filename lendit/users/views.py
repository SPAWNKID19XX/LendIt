
from rest_framework import permissions, status, generics
from .permissions import IsAuthenticatedAndIsOwner

from .serializers import CustomUserSerializers, CustomUserUpdateSerializers

from .models import CustomUser


# Create your views here.
class SignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomUserSerializers

class CustomUserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticatedAndIsOwner,)
    serializer_class = CustomUserUpdateSerializers

    def get_object(self):
        return self.request.user