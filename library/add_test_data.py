import os
import random

import django
import library
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")
django.setup()

from apitest.models import Author, Library, Book
from django.core.exceptions import ObjectDoesNotExist


fake = Faker()


# Создаем авторов
def create_authors(num_authors):
    authors = []
    for _ in range(num_authors):
        author = Author.objects.create(name=fake.name())
        authors.append(author)
    return authors


# Создаем библиотеки
def create_libraries(num_libraries):
    libraries = []
    for _ in range(num_libraries):
        library = Library.objects.create(
            name=fake.company(),
            location=fake.city()
        )
        libraries.append(library)
    return libraries


# Создаем книги
def create_books(num_books, authors, libraries):
    books = []
    for _ in range(num_books):
        author = random.choice(authors)
        library = random.choice(libraries)
        isbn = fake.unique.random_int(min=1000000000000, max=9999999999999)
        publish_date = fake.date_between(start_date='-50y', end_date='today')
        description = fake.paragraph()

        try:
            book = Book.objects.get(isbn=isbn)
        except ObjectDoesNotExist:
            book = Book(
                title=fake.catch_phrase(),
                isbn=isbn,
                library=library,
                author=author,
                publish_date=publish_date,
                description=description
            )
            book.save()
        books.append(book)
    return books


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", library.settings)
    django.setup()
    num_authors = 10  # Количество авторов
    num_libraries = 5  # Количество библиотек
    num_books = 50  # Количество книг

    authors = create_authors(num_authors)
    libraries = create_libraries(num_libraries)
    books = create_books(num_books, authors, libraries)

    print(f"Создано {len(authors)} авторов.")
    print(f"Создано {len(libraries)} библиотек.")
    print(f"Создано {len(books)} книг.")
