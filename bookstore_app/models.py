from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=180)
    country = models.CharField(max_length=120)

    class Meta:
        db_table = "bookstore_author"

    def __str__(self):
        return f"{self.name}--{self.country}"


class Book(models.Model):
    title = models.CharField(max_length=180)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = "bookstore_book"

    def __str__(self):
        return f"{self.title}--{self.price}--{self.author}"

# Create your models here.
# task

# >>> from bookstore_app.models import Author,Book
# >>> A=Author.objects.create(name="basheer",country="inida")
# >>> A1=Author.objects.create(name="shakespeare",country="uk")
# >>> A2=Author.objects.create(name="apj abdul kalam",country="india")
# >>> Book.objects.create(title="madhilukal",price=120,author=A)
# <Book: madhilukal--120--basheer--inida>
# >>> Book.objects.create(title="biography",price=450,author=A1)
# <Book: biography--450--shakespeare--uk>
# >>> Book.objects.create(title="wings",price=230,author=A2)
# <Book: wings--230--apj abdul kalam--india>
# >>> B=Book.objects.get(country="india")
# are: author, author_id, id, price, title
# >>> B=Book.objects.get(author__country="india")
# >>> print(B)
# wings--230--apj abdul kalam--india
# >>> Book.objects.filter(author__country="india")
# <QuerySet [<Book: wings--230--apj abdul kalam--india>]>
# >>> Book.objects.all()
# <QuerySet [<Book: madhilukal--120--basheer--inida>, <Book: biography--450--shakespeare--uk>, <Book: wings--230--apj abdul kalam--india>]>
# >>> Book.objects.filter(country="inida").update(country="india")
# >>> A3=Author.objects.create(name="python",country="usa")
# >>> Book.objects.create(title="Django Basics",price=780,author=A3)
# <Book: Django Basics--780--python--usa>
# >> Book.objects.filter(title="Django Basics")
# <QuerySet [<Book: Django Basics--780--python--usa>]>
# >>> Book.objects.filter(price__gt=300)
# <QuerySet [<Book: biography--450--shakespeare--uk>, <Book: Django Basics--780--python--usa>]>
# >>> for book in Book.objects.all():
# ...     print(f"{book.title} -- {book.price} -- {book.author.name} -- {book.author.country}")
# ...
# madhilukal -- 120 -- basheer -- india
# biography -- 450 -- shakespeare -- uk
# wings -- 230 -- apj abdul kalam -- india
# Django Basics -- 780 -- python -- usa
# >>>     print(f"{book.title} -- {book.author.name})
#   File "<console>", line 1
#     print(f"{book.title} -- {book.author.name})
# IndentationError: unexpected indent
# >>> for book in Book.objects.all():
# ...     print(f"{book.title} -- {book.author.name}")
# ...
# madhilukal -- basheer
# biography -- shakespeare
# wings -- apj abdul kalam
# Django Basics -- python
# >>> Book.objects.filter(price__gt=300)
