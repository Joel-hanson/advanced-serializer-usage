from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=60, blank=False)
    state_province = models.CharField(max_length=30, blank=False)
    country = models.CharField(max_length=50, blank=False)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=40, blank=False)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    USD = 'USD'
    CAD = 'CAD'
    EUR = 'EUR'
    AED = 'AED'
    CURRENCY_CHOICES = [
        (USD, 'US Dollar'),
        (CAD, 'Canadian Dollar'),
        (EUR, 'Euro'),
        (AED, 'United Arab Emirates Dirham'),
    ]
    title = models.CharField(max_length=100, blank=False)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    price = models.PositiveIntegerField()
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default=USD,
    )

    def __unicode__(self):
        return self.title