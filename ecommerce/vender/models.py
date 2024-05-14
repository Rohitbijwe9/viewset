from django.db import models

class Product(models.Model):
    pdate=models.DateTimeField(auto_now_add=True)
    pname=models.CharField(max_length=50)
    price=models.IntegerField()
    desc=models.TextField()


    def __str__(self):
        return self.pname