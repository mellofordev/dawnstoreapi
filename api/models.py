from django.db import models

# Create your models here.
product_type=(('dawn','dawn'),('addidas','addidas'),('nike','nike'))
class Product(models.Model):
    name = models.CharField(max_length=25)
    discription = models.TextField(max_length=300,blank=True,null=True)
    type = models.CharField(max_length=10, choices=product_type, default='dawn')
    pic = models.ImageField(upload_to='productpics',null=False)
    prize = models.IntegerField()

    def __str__(self) -> str:
        return self.name