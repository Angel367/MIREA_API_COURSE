import os

import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")
django.setup()

from apitest.models import Contact, PhoneNumber

fake = Faker()


# Создаем авторов
def generate_contacts_and_numbers(num_contacts):
    for _ in range(num_contacts):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()

        # Создание контакта
        contact = Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        # Создание случайных телефонных номеров для контакта
        for _ in range(2):  # Генерируем 2 номера для каждого контакта
            phone_number = fake.phone_number()
            phone_type = fake.random_element(elements=('mobile', 'home', 'work', 'other'))

            PhoneNumber.objects.create(
                contact=contact,
                phone_number=phone_number,
                phone_type=phone_type
            )


if __name__ == "__main__":
    num_contacts_to_generate = 10  # Измените на количество контактов, которое вы хотите создать
    generate_contacts_and_numbers(num_contacts_to_generate)
    print(f"Создано {num_contacts_to_generate} контактов и их телефонных номеров.")
