from django.contrib import admin
from django.urls import path
from Page1.views import OrderView, OrdersView, index
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='main_url'),
    url(r'order/(?P<id>\d+)', OrderView.as_view(), name='order_url'),
    url(r'orders/', OrdersView.as_view(), name='orders_url'),
]
