from django.db import models

# Create your models here.

class Categoey(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.name
    


class Books(models.Model):

    status_book = [
        ('availabe', 'availabe'),
        ('rental', 'rental'),
        ('sold', 'sold'),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True, null=True)
    photo_book = models.ImageField(upload_to='photos', blank=True, null=True)
    photo_author = models.ImageField(upload_to='photos', blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rental_per_day = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rental_period = models.IntegerField(blank=True, null=True)
    total_rent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_book, blank=True, null=True)
    category = models.ForeignKey(Categoey, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title
    