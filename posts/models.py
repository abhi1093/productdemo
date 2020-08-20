from django.db import models
import uuid

# Create your models here.
class Company(models.Model):
    company=models.CharField(max_length=40)
    GST=models.CharField(max_length=40)
    def __str__(self):
        return self.company

class Product(models.Model):
    Name=models.CharField(max_length=40)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    Cost=models.IntegerField()
    def __str__(self):
        return str(self.Name) + ": Rs." + str(self.Cost)

class PurchaseOrder(models.Model):
    purchase_order_number=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    product=models.ManyToManyField(Product)
    def __str__(self):
        return str(self.purchase_order_number)
    
