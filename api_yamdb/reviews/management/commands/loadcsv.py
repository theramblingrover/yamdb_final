import csv

from django.core.management.base import BaseCommand
from reviews.models import (Category, Comment, Genre, GenreTitle, Review,
                            Title, User)


class Command(BaseCommand):
    help = 'Upload .csv to DB'

    def load_users(self):
        filename = 'static/data/users.csv'
        self.stdout.write('Loading: Users')
        try:
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    try:
                        user, created = User.objects.get_or_create(**row)
                        if created:
                            self.stdout.write(f'Created {row}, {user}')
                        else:
                            self.stdout.write(f'{row} already exists')
                    except Exception as error:
                        self.stdout.write(f'Unable to create {row}, '
                                          f'error: {error}')
        except FileNotFoundError:
            self.stdout.write(f'File "{filename}" doesn\'t exist')
            exit(1)

    def load_category(self):
        filename = 'static/data/category.csv'
        self.stdout.write('Loading: Category')
        try:
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    try:
                        category, created = Category.objects.get_or_create(
                            **row)
                        if created:
                            self.stdout.write(f'Created {row}, {category}')
                        else:
                            self.stdout.write(f'{row} already exists')
                    except Exception as error:
                        self.stdout.write(f'Unable to create {row}, '
                                          f'error: {error}')
        except FileNotFoundError:
            self.stdout.write(f'File "{filename}" doesn\'t exist')
            exit(1)

    def load_genre(self):
        filename = 'static/data/genre.csv'
        self.stdout.write('Loading: Genre')
        try:
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    try:
                        genre, created = Genre.objects.get_or_create(**row)
                        if created:
                            self.stdout.write(f'Created {row}, {genre}')
                        else:
                            self.stdout.write(f'{row} already exists')
                    except Exception as error:
                        self.stdout.write(f'Unable to create {row}, '
                                          f'error: {error}')
        except FileNotFoundError:
            self.stdout.write(f'File "{filename}" doesn\'t exist')
            exit(1)

    def load_title(self):
        filename = 'static/data/titles.csv'
        self.stdout.write('Loading: Titles')
        try:
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    try:
                        title, created = Title.objects.get_or_create(
                            pk=row['id'],
                            name=row['name'],
                            year=int(row['year']),
                            category=Category.objects.get(pk=int(
                                                          row['category']))
                        )
                        if created:
                            self.stdout.write(f'Created: {title}, {row}')
                        else:
                            self.stdout.write(f'{row} already exists')
                    except Exception as error:
                        self.stdout.write(f'Unable to create {row}, '
                                          f'error: {error}')
        except FileNotFoundError:
            self.stdout.write(f'File "{filename}" doesn\'t exist')
            exit(1)

    def load_genre_title(self):
        filename = 'static/data/genre_title.csv'
        self.stdout.write('Loading: Genre-Titles')
        try:
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    try:
                        genre_title, created = (
                            GenreTitle.objects.get_or_create(
                                pk=row['id'],
                                genre=Genre.objects.get(pk=int(
                                                        row['genre_id'])),
                                title=Title.objects.get(pk=int(
                                                        row['title_id']))
                            )
                        )
                        if created:
                            self.stdout.write(f'Created: {genre_title}, {row}')
                        else:
                            self.stdout.write(f'{row} already exists')
                    except Exception as error:
                        self.stdout.write(f'Unable to create {row}, '
                                          f'error: {error}')
        except FileNotFoundError:
            self.stdout.write(f'File "{filename}" doesn\'t exist')
            exit(1)

    def load_review(self):
        filename = 'static/data/review.csv'
        self.stdout.write('Loading: Reviews')
        try:
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    try:
                        title, created = Review.objects.get_or_create(
                            pk=row['id'],
                            title=Title.objects.get(pk=int(row['title_id'])),
                            text=row['text'],
                            author=User.objects.get(pk=int(row['author'])),
                            score=row['score'],
                            pub_date=row['pub_date']
                        )
                        if created:
                            self.stdout.write(f'Created: {title}, {row}')
                        else:
                            self.stdout.write(f'{row} already exists')
                    except Exception as error:
                        self.stdout.write(f'Unable to create {row}, '
                                          f'error: {error}')

        except FileNotFoundError:
            self.stdout.write(f'File "{filename}" doesn\'t exist')
            exit(1)

    def load_comment(self):
        filename = 'static/data/comments.csv'
        self.stdout.write('Loading: Comments')
        try:
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                for row in reader:
                    try:
                        title, created = Comment.objects.get_or_create(
                            pk=row['id'],
                            review=Review.objects.get(pk=int(
                                                      row['review_id'])),
                            text=row['text'],
                            author=User.objects.get(pk=int(row['author'])),
                            pub_date=row['pub_date']
                        )
                        if created:
                            self.stdout.write(f'Created: {title}, {row}')
                        else:
                            self.stdout.write(f'{row} already exists')
                    except Exception as error:
                        self.stdout.write(f'Unable to create {row}, '
                                          f'error: {error}')
        except FileNotFoundError:
            self.stdout.write(f'File "{filename}" doesn\'t exist')
            exit(1)

    def handle(self, *args, **options):
        self.load_users()
        self.load_category()
        self.load_genre()
        self.load_title()
        self.load_genre_title()
        self.load_review()
        self.load_comment()
