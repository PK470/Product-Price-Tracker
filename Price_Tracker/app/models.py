from django.db import models
from .price_checker import Price

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=1000, blank = True)
    url = models.URLField()
    current_price = models.FloatField(blank = True)
    old_price = models.FloatField(blank = True)
    price_difference = models.FloatField(blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.name)
    class Meta:
        ordering = ('price_difference','-created')
    
    def save(self, *args, **kwargs):
        price, name  = Price.check_price(self.url)
        if price is None and name is None:
            print("Error : Can't Save")
        else:
            old_price = self.current_price
            if self.current_price is not None:
                if price is not None and price != old_price:
                    diff = price - old_price
                    self.price_difference = round(diff, 2)
                    self.old_price = old_price
                    self.current_price = price
            else:
                self.old_price = 0
                self.difference = 0
            self.name = name
            self.current_price = price
            print("Saved")
            super().save(*args, **kwargs)

    