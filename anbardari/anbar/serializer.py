from rest_framework import serializers

from .models import *


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'pk',
            'quantity',
            'order_status',
            'total_price',
            'order_date',
            'customer',
            'product'
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'pk',
            'quantity',
            'price',
            'name',
            'supplier'
        ]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'pk',
            'Address',
            'Name'
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'pk',
            'Name',
            'phone',
            'employee'
        ]


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'pk',
            'address',
            'email',
            'name'
        ]
