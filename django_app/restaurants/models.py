from django.db import models

PRICE_RANGE = (
    ('LT10', 'LessThen10'),
    ('GE10', 'GreaterEqual10'),
    ('GE20', 'GreaterEqual20'),
)

CUISINE = (
    ('KOR', 'KoreaCuisine'),
    ('JAP', 'JapanCuisine'),
    ('CHI', 'ChinaCuisine'),
    ('WES', 'WesternCuisine'),
    ('WOR', 'WorldCuisine'),
    ('BUF', 'Buffet'),
    ('CAF', 'Cafe'),
    ('PUB', 'Pub'),
)


class restaurant(models.Model):
    title = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=20, decimal_places=15)
    longitude = models.DecimalField(max_digits=20, decimal_places=15)
    price_range = models.CharField(max_length=4, choices=PRICE_RANGE)
    cuisine = models.CharField(max_length=3, choices=CUISINE)
