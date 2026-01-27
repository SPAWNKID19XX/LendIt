from decimal import Decimal

from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from django.conf import settings


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class City(models.TextChoices):
    LISBON = "LIS", "Lisbon"
    PORTO = "OPO", "Porto"
    VILA_NOVA_DE_GAIA = "VNG", "Vila Nova de Gaia"
    SINTRA = "SIN", "Sintra"
    CASCAIS = "CAS", "Cascais"
    AMADORA = "AMA", "Amadora"
    COIMBRA = "COI", "Coimbra"
    BRAGA = "BRA", "Braga"
    SETUBAL = "SET", "Setúbal"
    AVEIRO = "AVE", "Aveiro"
    FARO = "FAO", "Faro"
    GUIMARAES = "GUI", "Guimarães"
    VISEU = "VIS", "Viseu"
    LEIRIA = "LEI", "Leiria"
    EVORA = "EVO", "Évora"
    PORTIMAO = "PRM", "Portimão"
    FUNCHAL = "FNC", "Funchal"

class Item(models.Model):
    title = models.CharField(max_length=50, validators=[MinLengthValidator(5)])
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='items')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='items')
    city = models.CharField(max_length=50, choices=City.choices, default=City.LISBON.value)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('1.00'))])

class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='itemImages')
