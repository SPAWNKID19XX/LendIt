from rest_framework import serializers
from users.serializers  import ShortCustomUserSerializer

from .models import ItemImage, Item


class ItemImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    images = ItemImagesSerializers(many=True)
    owner = ShortCustomUserSerializer(read_only=True)
    city_display_name = serializers.CharField(source='get_city_display', read_only=True)
    class Meta:
        model = Item
        fields = ['title', 'description','owner','images', 'category','price','city','city_display_name']


    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        images = validated_data.pop('images')
        item = Item.objects.create(**validated_data)

        lst = [ItemImage(item=item, **image) for image in images]

        ItemImage.objects.bulk_create(lst)

        return item

