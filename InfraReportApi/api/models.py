from django.db import models

class Product(models.Model):#table
    name = models.CharField(max_length=100)#database column
    price = models.DecimalField(max_digits=5, decimal_places=2)#database column
    description = models.TextField()#database column
    created_at = models.DateTimeField(auto_now_add=True)#database column
    updated_at = models.DateTimeField(auto_now=True)#database column

    def __str__(self):
        return self.name#The instance name when we use print(object) will be self.name