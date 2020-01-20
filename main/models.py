from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    categoryName = models.CharField(max_length=20)

    def __str__(self):
        return self.categoryName


class Type(models.Model):
    typeName = models.CharField(max_length=20)

    def __str__(self):
        return self.typeName


class User(models.Model):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    gender = models.CharField(max_length=1, choices=(('F', 'Female'), ('M', 'Male'),))
    zipCode = models.CharField(max_length=8)

    def __str__(self):
        return self.gender + " " + self.zipCode


class Peripheral(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ManyToManyField(Category)
    types = models.ManyToManyField(Type)
    ratings = models.ManyToManyField(User, through="Rating")

    def __str__(self):
        return self.movieTitle


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    peripheral = models.ForeignKey(Peripheral, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.rating)
