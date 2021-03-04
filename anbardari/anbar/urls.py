from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('product/', ProductListApiView.as_view()),
    re_path('product/(?P<pk>\d+)/$', ProductDetailApiView.as_view()),
   
    path('order/', OrderListApiView.as_view()),
    re_path('order/(?P<pk>\d+)/$', OrderDetailApiView.as_view()),
  
    path('customer/', CustomerListApiView.as_view()),
    re_path('customer/(?P<pk>\d+)/$', CustomerDetailApiView.as_view()),
  
    path('supplier/', SupplierListApiView.as_view()),
    re_path('supplier/(?P<pk>\d+)/$', SupplierDetailApiView.as_view()),
    
    path('employee/', EmployeeListApiView.as_view()),
    re_path('employee/(?P<pk>\d+)/$', EmployeeDetailApiView.as_view())
]
