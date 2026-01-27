import random
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from faker import Faker
from items.models import Category

CATEGORY_CHOICES = [
    'cars',           # Легковые авто, внедорожники
    'tools',          # Перфораторы, лестницы, садовая техника
    'electronics',    # Камеры, игровые приставки, проекторы
    'property',       # Квартиры, офисы, коворкинги
    'equipment',      # Промышленное или строительное оборудование
    'sportswear',     # Сноуборды, велосипеды, палатки
    'events',         # Звук, свет, мебель для вечеринок, костюмы
    'appliances',     # Бытовая техника (пылесосы, моющие машины)
    'transport',      # Самокаты, прицепы, грузовики
    'medical',        # Коляски, костыли, реабилитационное оборудование
    'toys',           # Детские товары, батуты, манежи
    'hobbies'         # Музыкальные инструменты, настольные игры
]

class Command(BaseCommand):
    help = "Creates new categories"

    def handle(self, *args, **options):
        self.stdout.write("Add new categories...")
        lst = []
        for category in CATEGORY_CHOICES:
            cat_item = Category(
                name=category,
                slug=category,
            )
            lst.append(cat_item)


        Category.objects.bulk_create(lst)
        self.stdout.write("categories ware created!")
