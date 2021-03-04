from django.db import models

ORDER_STATUS = [('re', 'ready'), ('co', 'complete'), ('se', 'sent'), ('pe', 'pending')]


class Employee(models.Model):
    Address = models.CharField(max_length=200)
    Name = models.CharField(max_length=40)

    def __str__(self):
        return self.Name


class Customer(models.Model):
    Name = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Supplier(models.Model):
    address = models.CharField(max_length=200)
    email = models.EmailField()
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Product(models.Model):
    quantity = models.IntegerField()
    price = models.FloatField()
    name = models.CharField(max_length=40)
    supplier = models.ForeignKey(to=Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    quantity = models.IntegerField()
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS)
    total_price = models.FloatField()
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(to=Product)

    # def __str__(self):
    #     return self.
