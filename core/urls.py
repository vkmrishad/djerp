from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^contacts/new$', views.new_contact, name='new_contact'),
    url(r'^contacts/add$', views.add_contact, name='add_contact'),
    url(r'^items$', views.items, name='items'),
    url(r'^items/new$', views.new_item, name='new_item'),
    url(r'^items/add$', views.add_item, name='add_item'),
    url(r'^sales-orders$', views.sales_orders, name='sales_orders'),
    url(r'^sales-orders/new$', views.new_sales_orders, name='new_sales_orders'),
    url(r'^sales-orders/add$', views.add_sales_orders, name='add_sales_orders'),
    url(r'^sales-orders/get-item$', views.sales_orders_get_item, name='sales_orders_get_item'),
    url(r'^delivery-orders/new$', views.new_delivery_orders, name='new_delivery_orders'),
    url(r'^delivery-orders/add$', views.add_delivery_orders, name='add_delivery_orders'),
    url(r'^delivery-orders/get-item$', views.delivery_orders_get_item, name='delivery_orders_get_item'),
]