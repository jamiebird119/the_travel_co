from django.db import models
from django.contrib.postgres.fields import ArrayField
import jsonfield

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30, )
    id = models.CharField(max_length=30, primary_key=True,)
    href = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Region(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=100)
    href = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=100)
    href = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=100)
    href = models.URLField()
    description = models.CharField(max_length=3000, null=True)
    category_type = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name


class Tour(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    href = models.URLField(max_length=300)
    name = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)
    product_line = models.CharField(max_length=300)
    departures_start_date = models.DateField(null=True)
    departures_end_date = models.DateField(null=True)
    description = models.CharField(max_length=2000)
    booking_company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
    structured_itineraries = models.CharField(max_length=2000, null=True)
    category = models.ManyToManyField('Category', blank=True)
    details = jsonfield.JSONField()
    images = jsonfield.JSONField()
    site_links = models.JSONField()
    tour = models.CharField(max_length=300)
    departures_href = models.URLField()
    departures_list = ArrayField(
        models.DateField(null=True),
        max_length=3000, null=True)
    from_price = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    region = models.ForeignKey("Region", on_delete=models.CASCADE)
    start_country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True, related_name="start_country")
    finish_country = models.ForeignKey('Country', on_delete=models.CASCADE, null=True, related_name="finish_country")
    visited_countries = models.ManyToManyField('Country', blank=True, related_name="visited_countries")

    def __str__(self):
        return self.name
    