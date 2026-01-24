
from rest_framework import permissions, status, generics
from .serializers import CustomUserSerializers

from .models import CustomUser


# Create your views here.
class SignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomUserSerializers