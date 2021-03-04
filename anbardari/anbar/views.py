from django.shortcuts import render
from rest_framework import generics, mixins
from .serializer import *


class ProductDetailApiView(
    generics.RetrieveAPIView,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ProductListApiView(
    generics.ListAPIView,
    mixins.CreateModelMixin
):
    authentication_classes = []
    permission_classes = []
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class OrderDetailApiView(
    generics.RetrieveAPIView,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    authentication_classes = []
    permission_classes = []
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class OrderListApiView(
    generics.ListAPIView,
    mixins.CreateModelMixin
):
    authentication_classes = []
    permission_classes = []
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class SupplierDetailApiView(
    generics.RetrieveAPIView,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    authentication_classes = []
    permission_classes = []
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class SupplierListApiView(
    generics.ListAPIView,
    mixins.CreateModelMixin
):
    authentication_classes = []
    permission_classes = []
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CustomerDetailApiView(
    generics.RetrieveAPIView,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    authentication_classes = []
    permission_classes = []
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CustomerListApiView(
    generics.ListAPIView,
    mixins.CreateModelMixin
):
    authentication_classes = []
    permission_classes = []
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class EmployeeDetailApiView(
    generics.RetrieveAPIView,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    authentication_classes = []
    permission_classes = []
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class EmployeeListApiView(
    generics.ListAPIView,
    mixins.CreateModelMixin
):
    authentication_classes = []
    permission_classes = []
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
