from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class MainAutoTableModels(models.Model):
    articles = models.CharField(max_length=255, blank=True, verbose_name='Articles')
    group = models.CharField(max_length=255, blank=True, verbose_name='Group')
    subgroup = models.CharField(max_length=255, blank=True, verbose_name='SubGroup')
    vendor = models.CharField(max_length=255, blank=True, verbose_name='Vendor')
    vendor_code = models.CharField(max_length=255, blank=True, verbose_name='Vendor Code')
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)], verbose_name='Quantity')
    req_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)], verbose_name='Required quantity')
    auto_brand = models.CharField(max_length=255, blank=True, verbose_name='Brand')
    auto_model = models.CharField(max_length=255, blank=True, verbose_name='Model')
    purchase_price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Purchase price')
    selling_price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Selling price')
    recommend_price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Recommend price')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    content = models.TextField(blank=True)
    content_extra1 = models.TextField(blank=True)
    content_extra2 = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    margin = models.FloatField(default=1.7, validators=[MinValueValidator(0)])
    provider = models.CharField(max_length=255, blank=True, verbose_name='Provider')
    currency = models.CharField(max_length=255, blank=True, verbose_name='Currency')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.articles

