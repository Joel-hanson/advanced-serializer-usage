from random import choice
from autofixture import AutoFixture
from .models import Publisher, Author, Book



def fake_publisher(count=10):
    fixture = AutoFixture(Publisher)
    entries = fixture.create(count)

def fake_author(count=10):
    fixture = AutoFixture(Author)
    entries = fixture.create(count)


def fake_book(count=10):
    fixture = AutoFixture(Book)
    entries = fixture.create(count, commit=False)
    for entry in entries:
        entry.currency=choice([entry.USD, entry.CAD ,entry.EUR ,entry.AED])
        entry.save()
        entry.authors.add(choice(Author.objects.values_list('id', flat=True)))
