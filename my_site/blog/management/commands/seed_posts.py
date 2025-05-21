from django.core.management.base import BaseCommand
from django.utils.text import slugify
from ...models import Author, Post, Tag
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Seeds the database with sample posts, authors, and tags'

    def handle(self, *args, **kwargs):
        # Create Tags
        tag_names = ['Django', 'Python', 'Web Dev', 'Tutorial', 'News']
        tags = []
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(caption=name)
            tags.append(tag)

        # Create Authors
        author_data = [
            ('Alice', 'Smith', 'alice@gmail.com'),
            ('Bob', 'Johnson', 'bob@gmail.com'),
            ('Carol', 'Williams', 'carol@gmail.com'),
        ]
        authors = []
        for first_name, last_name, email in author_data:
            author, created = Author.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                email_address=email
            )
            authors.append(author)

        # Create Posts
        for i in range(10):
            title = f'Sample Post {i + 1}'
            post = Post.objects.create(
                title=title,
                excerpt='This is a short excerpt of the blog post.',
                content='Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' * 5,
                image_name=f'image{i + 1}.jpg',
                date=date.today() - timedelta(days=i),
                slug=slugify(title),
                author=random.choice(authors)
            )
            post.tags.set(random.sample(tags, k=random.randint(1, 3)))

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))
