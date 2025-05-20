from django.core.management.base import BaseCommand
from django.core.validators import MinValueValidator, MaxValueValidator
from ...models import Book
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generates sample books for the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=50,
            help='Number of books to create (default: 50)',
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing books before generation',
        )

    def handle(self, *args, **options):
        fake = Faker()
        count = options['count']

        if options['clear']:
            Book.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Cleared existing books'))

        books = []
        popular_authors = [
            'J.K. Rowling',
            'Stephen King',
            'George R.R. Martin',
            'Agatha Christie',
            'Dan Brown'
        ]

        for _ in range(count):
            is_bestselling = random.random() < 0.3
            author = random.choice(popular_authors) if random.random() < 0.7 else fake.name()

            books.append(Book(
                title=fake.sentence(nb_words=3)[:-1],
                rating=random.randint(1, 5),
                author=author,
                is_bestselling=is_bestselling
            ))

        Book.objects.bulk_create(books)
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {count} books')
        )