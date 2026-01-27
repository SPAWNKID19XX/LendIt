import random
from django.conf import settings
from django.core.management import BaseCommand
from items.models import Category, Item, City, ItemImage

class Command(BaseCommand):
    help = "Creates new Items"
    all_items = list(Item.objects.all())
    def handle(self, *args, **options):
        self.stdout.write("Add new ITEMSIMGS...")
        lst = []
        img_path = f'{settings.BASE_DIR}/test_img.jpg'
        print(img_path)
        for item in self.all_items:
            for obj in range(random.randint(3, 5)):
                item_imgs = ItemImage(
                    item=item,
                    image = img_path,
                )
                lst.append(item_imgs)

        ItemImage.objects.bulk_create(lst)

        self.stdout.write("items ware created!")
