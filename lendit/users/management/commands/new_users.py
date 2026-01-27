import random
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from faker import Faker


class Command(BaseCommand):
    help = "Creates new users"

    def handle(self, *args, **options):
        fake = Faker()
        User = get_user_model()
        create_users_list = []

        for i in range(50):
            unique_email = fake.unique.email()
            user = User(
                email=unique_email,
                first_name=fake.first_name(),
                last_name=fake.last_name(),

                is_staff= False,
                is_superuser= False,
                is_active= True,
                is_renter = True,

                tlf = random.randint(1,1000000)
            )
            user.set_password('admin')
            create_users_list.append(user)
        self.stdout.write("Add new users...")
        User.objects.bulk_create(create_users_list)

        self.stdout.write("users ware created!")
