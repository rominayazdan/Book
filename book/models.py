from django.db import models
from user.models import User


class BaseBook(models.Model):
    name = models.CharField(max_length=50)
    published_date = models.DateField()


    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Book(BaseBook):

    CATEGORY_CHOICES = [
        ('SC', 'Science'),
        ('FN', 'Fun'),
        ('HC', 'Historical'),
    ]
    price = models.IntegerField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, db_index=True)
    is_published = models.BooleanField(default=True)
    #Related column to user model
    added = models.ForeignKey(User, related_name="books", on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class ImageBook(models.Model):
    name = models.CharField(max_length=50, verbose_name="Image Name")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="images", related_query_name="image_query")

    class Meta:
        verbose_name = "Images of Book"

    def __str__(self):
        return self.name





