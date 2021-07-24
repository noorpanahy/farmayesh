from django.db import models

# Create your models here.

class Registration(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=64)
    Lname = models.CharField(max_length=32)
    Email = models.EmailField(max_length=74, unique=True)
    Pnum = models.IntegerField(unique=True)
    address = models.CharField(max_length=128)

class Resturant(models.Model):
    ResID = models.AutoField(primary_key=True)
    Resname = models.CharField(max_length=128)
    Logo = models.FileField()
    Slogan = models.TextField(max_length=255)

class Catagure(models.Model):
    CaID = models.AutoField(primary_key=True)
    Canam = models.CharField(max_length=32,unique=True)

class Food(models.Model):
    FoodID = models.AutoField(primary_key=True)
    ResID = models.ForeignKey(Resturant,on_delete=models.CASCADE)
    CaID = models.ForeignKey(Catagure,on_delete=models.CASCADE)
    Foodname = models.CharField(max_length=32,unique=True)
    price = models.IntegerField()
    Discount = models.IntegerField()
    pic = models.FileField()

class OrderItem(models.Model):
    OrderItemID = models.AutoField(primary_key=True)
    FoodID = models.ForeignKey(Food,on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Allprice = models.IntegerField()

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    Ordate = models.DateField(max_length=32)
    CustomerID = models.ForeignKey(Registration,on_delete=models.CASCADE)
    OrderItemID = models.ForeignKey(OrderItem,on_delete=models.CASCADE)

class Administrator(models.Model):
    Username = models.CharField(max_length=32,unique=True)
    Password = models.CharField(max_length=64)







    
