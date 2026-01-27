import random
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from faker import Faker
from items.models import Category, Item, City

class Command(BaseCommand):
    help = "Creates new Items"
    all_users = list(get_user_model().objects.all())
    all_categories = list(Category.objects.all())
    all_cities = City.values
    def handle(self, *args, **options):
        self.stdout.write("Add new ITEMS...")
        faker = Faker()
        lst = []
        for item in range(5000):
            item = Item(
                title=faker.word(),
                description=faker.texts(),
                owner=random.choice(self.all_users),
                category=random.choice(self.all_categories),
                city = random.choice(self.all_cities),
                price=faker.pydecimal(min_value=0, max_value=100),
            )
            lst.append(item)



        Item.objects.bulk_create(lst)
        self.stdout.write("items ware created!")
