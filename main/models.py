from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(models.Model):
    username = models.CharField(max_length=20, default="nickname")
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    gender = models.CharField(max_length=1, choices=(('F', 'Female'), ('M', 'Male'),))
    zipCode = models.CharField(max_length=8)

    def __str__(self):
        return self.username


class Peripheral(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    type_db = models.CharField(max_length=100)
    stars = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    peripheral = models.ForeignKey(Peripheral, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.rating)
