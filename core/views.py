from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect	
from django.core import serializers
import json	
from django.contrib import messages
from .models import Contact,Item,ItemGroup,SalesOrder,SalesOrderItem


def index(request):
	return redirect('/dashboard')	

def dashboard(request):
	return render(request, 'inventory/dashboard.html')		

def contacts(request):
	all_contacts = Contact.objects.all()
	return render(request, 'inventory/contacts.html',{'contact_list':all_contacts})	

def new_contact(request):
	return render(request, 'inventory/new-contact.html')	

def add_contact(request):
	if request.method == 'POST':
		salutation = request.POST.get("salutation")
		first_name = request.POST.get("first_name")
		last_name = request.POST.get("last_name")
		company_name = request.POST.get("company_name")
		contact_display_name = request.POST.get("contact_display_name")
		contact_email = request.POST.get("contact_email")
		contact_workplace = request.POST.get("contact_workplace")
		contact_mobile = request.POST.get("contact_mobile")
		contact_website = request.POST.get("contact_website")
		contact_type = request.POST.get("contact_type")
		bill_attention = request.POST.get("bill_attention")
		bill_address1 = request.POST.get("bill_address1")
		bill_address2 = request.POST.get("bill_address2")
		bill_city = request.POST.get("bill_city")
		bill_state = request.POST.get("bill_state")
		bill_zip = request.POST.get("bill_zip")
		bill_country = request.POST.get("bill_country")
		bill_fax = request.POST.get("bill_fax")
		bill_phone = request.POST.get("bill_phone")
		ship_attention = request.POST.get("ship_attention")
		ship_address1 = request.POST.get("ship_address1")
		ship_address2 = request.POST.get("ship_address2")
		ship_city = request.POST.get("ship_city")
		ship_state = request.POST.get("ship_state")
		ship_zip = request.POST.get("ship_zip")
		ship_country = request.POST.get("ship_country")
		ship_fax = request.POST.get("ship_fax")
		ship_phone = request.POST.get("ship_phone")


		contact = Contact(salutation=salutation,first_name=first_name,last_name=last_name,company_name=company_name,contact_display_name=contact_display_name,contact_email=contact_email,contact_workplace=contact_workplace,contact_mobile=contact_mobile,contact_website=contact_website,contact_type=contact_type,bill_attention=bill_attention,bill_address1=bill_address1,bill_address2=bill_address2,bill_city=bill_city,bill_state=bill_state,bill_zip=bill_zip,bill_country=bill_country,bill_fax=bill_fax,bill_phone=bill_phone,ship_attention=ship_attention,ship_address1=ship_address1,ship_address2=ship_address2,ship_city=ship_city,ship_state=ship_state,ship_zip=ship_zip,ship_country=ship_country,ship_fax=ship_fax,ship_phone=ship_phone)

		contact.save()

		data = {'success':True,'msg':'Store user data successfully'}

		return HttpResponse(json.dumps(data),content_type="application/json")

	else:
		return HttpResponse(json.dumps(data),content_type="application/json")

def items(request):
	all_items = Item.objects.all()
	return render(request, 'inventory/items.html',{'item_list':all_items})	

def new_item(request):
	return render(request, 'inventory/new-item.html')

def add_item(request):
	if request.method == 'POST':
		item_type = request.POST.get("item_type")
		item_name = request.POST.get("item_name")
		sku = request.POST.get("sku")
		unit = request.POST.get("unit")
		sale_price = request.POST.get("sale_price")
		sale_account = request.POST.get("sale_account")
		sale_desc = request.POST.get("sale_desc")
		tax = request.POST.get("tax")
		purchase_price = request.POST.get("purchase_price")
		purchase_account = request.POST.get("purchase_account")
		purchase_desc = request.POST.get("purchase_desc")
		inv_account = request.POST.get("inv_account")
		inv_reorder_level = request.POST.get("inv_reorder_level")
		inv_opening_stock = request.POST.get("inv_opening_stock")
		inv_opening_stock_value = request.POST.get("inv_opening_stock_value")

		item = Item(item_type = item_type,item_name = item_name,sku = sku,unit = unit,sale_price = sale_price,sale_account = sale_account,sale_desc = sale_desc,tax = tax,purchase_price = purchase_price,purchase_account = purchase_account,purchase_desc = purchase_desc,inv_account = inv_account,inv_reorder_level = inv_reorder_level,inv_opening_stock = inv_opening_stock,inv_opening_stock_value = inv_opening_stock_value)

		item.save()

		data = {'success':True,'msg':'Store user data successfully'}

		return HttpResponse(json.dumps(data),content_type="application/json")

	else:
		return HttpResponse(json.dumps(data),content_type="application/json")	

def sales_orders(request):
	all_so = SalesOrder.objects.all()
	return render(request, 'inventory/sales-orders.html',{'so_list':all_so})	

def new_sales_orders(request):
	all_contacts = Contact.objects.all()
	all_items = Item.objects.all()
	all_itemgroups = ItemGroup.objects.all()
	return render(request, 'inventory/new-sales-orders.html',{'contact_list':all_contacts,'item_list':all_items,'item_group_list':all_itemgroups})	

#@csrf_protect
@csrf_exempt
def sales_orders_get_item(request):
	if request.method == 'POST':
		
		get_item = json.loads(request.body)
		item = get_item['item']

		data = serializers.serialize('json', Item.objects.filter(item_color='Red',item_group_name=item,item_size='S'))
		print ("Data",json.loads(data)[0]['fields'])
		item_rate = json.loads(data)[0]['fields']['sale_price']
		item_id = json.loads(data)[0]['fields']['item_id']
		return HttpResponse(json.dumps({'item_rate':item_rate,'item_id':item_id}),content_type="application/json")
	return HttpResponse(json.dumps({"all_items":"aasda"}),content_type="application/json")		

@csrf_exempt
def add_sales_orders(request):
	if request.method == 'POST':
		try:
			get_content = json.loads(request.body)
			items = get_content['items']
			so_number = get_content['order_no']
			so_customer = get_content['customer_id']
			so_reference = get_content['reference_no']
			so_date = get_content['date']
			so_total = get_content['total']

			salesorders = SalesOrder(so_number = so_number,so_customer = so_customer,so_reference = so_reference,so_date = so_date,so_amount=so_total)
			salesorders.save()

			for item in items:
				salesitem = SalesOrderItem(so_number = so_number,so_item_id = item['Id'],so_item_qty = item['Quantity'],so_item_rate = item['Amount'])
				salesitem.save()

			data = {'success':True,'msg':'Sales Order has been created'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		except ValueError:
			data = {'success':False,'msg':'Something went wrong!'}
			return HttpResponse(json.dumps(data),content_type="application/json")

	else:
		data = {'success':False,'msg':'Something went wrong!'}
		return HttpResponse(json.dumps(data),content_type="application/json")	


def new_delivery_orders(request):
	all_contacts = Contact.objects.all()
	all_items = Item.objects.all()
	all_itemgroups = ItemGroup.objects.all()
	return render(request, 'inventory/new-delivery-orders.html',{'contact_list':all_contacts,'item_list':all_items,'item_group_list':all_itemgroups})	

@csrf_exempt
def add_delivery_orders(request):
	if request.method == 'POST':
		try:
			get_content = json.loads(request.body)
			items = get_content['items']
			so_number = get_content['order_no']
			so_customer = get_content['customer_id']
			so_reference = get_content['reference_no']
			so_date = get_content['date']
			so_total = get_content['total']

			salesorders = SalesOrder(so_number = so_number,so_customer = so_customer,so_reference = so_reference,so_date = so_date,so_amount=so_total)
			salesorders.save()

			# for item in items:
			# 	salesitem = SalesOrderItem(so_number = so_number,so_item_id = item['Id'],so_item_qty = item['Quantity'],so_item_rate = item['Amount'])
			# 	salesitem.save()

			data = {'success':True,'msg':'Sales Order has been created'}
			return HttpResponse(json.dumps(data),content_type="application/json")
		except ValueError:
			data = {'success':False,'msg':'Something went wrong!'}
			return HttpResponse(json.dumps(data),content_type="application/json")

	else:
		data = {'success':False,'msg':'Something went wrong!'}
		return HttpResponse(json.dumps(data),content_type="application/json")	


@csrf_exempt
def delivery_orders_get_item(request):
	if request.method == 'POST':
		
		get_item = json.loads(request.body)
		item = get_item['item']

		data = serializers.serialize('json', Item.objects.filter(item_color='Red',item_group_name=item,item_size='S'))
		print ("Data",json.loads(data)[0]['fields'])
		item_rate = json.loads(data)[0]['fields']['sale_price']
		item_id = json.loads(data)[0]['fields']['item_id']
		return HttpResponse(json.dumps({'item_rate':item_rate,'item_id':item_id}),content_type="application/json")
	return HttpResponse(json.dumps({"all_items":"aasda"}),content_type="application/json")				