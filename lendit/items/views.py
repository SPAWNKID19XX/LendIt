from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Item
from .serializers import ItemSerializer
from .permissions import ItemsGetAllowAnyCreateAuthUpdateDeleteOwner


# Create your views here.
class ItemListAPIViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = (ItemsGetAllowAnyCreateAuthUpdateDeleteOwner,)

    def get_queryset(self):
        queryset = Item.objects.select_related(
            'owner',
            'category'
        ).prefetch_related(
            "images"
        ).all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)