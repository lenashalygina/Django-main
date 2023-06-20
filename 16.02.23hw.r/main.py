from django.test import TestCase
from models import Book

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls)
        Book.objects.create(
            title='The Great Gatsby',
            author='F. Scott Fitzgerald',
            publication_year=1925,
        )

    def test_book_title(self):
        book = Book.objects.get(id=1)
        expected_title = 'The Great Gatsby'
        self.assertEqual(book.title, expected_title)

    def test_book_author(self):
        book = Book.objects.get(id=1)
        expected_author = 'F. Scott Fitzgerald'
        self.assertEqual(book.author, expected_author)

    def test_book_publication_year(self):
        book = Book.objects.get(id=1)
        expected_year = 1925
        self.assertEqual(book.publication_year, expected_year)

    def test_book_creation(self):
        book_count = Book.objects.count()
        self.assertEqual(book_count, 1)

    def test_book_update(self):
        book = Book.objects.get(id=1)
        new_title = 'Updated Title'
        book.title = new_title
        book.save()
        updated_book = Book.objects.get(id=1)
        self.assertEqual(updated_book.title, new_title)

    def test_book_deletion(self):
        book = Book.objects.get(id=1)
        book.delete()
        book_count = Book.objects.count()
        self.assertEqual(book_count, 0)
