from django.db import models

class Contact(models.Model):
    salutation = models.CharField(max_length=30,null=True,blank=True)
    first_name = models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=30,null=True,blank=True)
    company_name = models.CharField(max_length=30,null=True,blank=True)
    contact_display_name = models.CharField(max_length=30,null=True,blank=True)
    contact_email = models.CharField(max_length=30,null=True,blank=True)
    contact_workplace = models.CharField(max_length=30,null=True,blank=True)
    contact_mobile = models.CharField(max_length=30,null=True,blank=True)
    contact_website = models.CharField(max_length=30,null=True,blank=True)
    contact_type = models.CharField(max_length=30,null=True,blank=True)
    bill_attention = models.CharField(max_length=30,null=True,blank=True)
    bill_address1 = models.CharField(max_length=30,null=True,blank=True)
    bill_address2 = models.CharField(max_length=30,null=True,blank=True)
    bill_city = models.CharField(max_length=30,null=True,blank=True)
    bill_state = models.CharField(max_length=30,null=True,blank=True)
    bill_zip = models.CharField(max_length=30,null=True,blank=True)
    bill_country = models.CharField(max_length=30,null=True,blank=True)
    bill_fax = models.CharField(max_length=30,null=True,blank=True)
    bill_phone = models.CharField(max_length=30,null=True,blank=True)
    ship_attention = models.CharField(max_length=30,null=True,blank=True)
    ship_address1 = models.CharField(max_length=30,null=True,blank=True)
    ship_address2 = models.CharField(max_length=30,null=True,blank=True)
    ship_city = models.CharField(max_length=30,null=True,blank=True)
    ship_state = models.CharField(max_length=30,null=True,blank=True)
    ship_zip = models.CharField(max_length=30,null=True,blank=True)
    ship_country = models.CharField(max_length=30,null=True,blank=True)
    ship_fax = models.CharField(max_length=30,null=True,blank=True)
    ship_phone = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.first_name

class Item(models.Model):
    item_id = models.CharField(max_length=30,null=True,blank=True)
    item_group_id = models.CharField(max_length=30,null=True,blank=True)
    item_group_name = models.CharField(max_length=30,null=True,blank=True)
    item_type = models.CharField(max_length=30,null=True,blank=True)
    item_name = models.CharField(max_length=30,null=True,blank=True)
    item_color = models.CharField(max_length=30,null=True,blank=True)
    item_size = models.CharField(max_length=30,null=True,blank=True)
    sku = models.CharField(max_length=30,null=True,blank=True)
    unit = models.CharField(max_length=30,null=True,blank=True)
    sale_price = models.CharField(max_length=30,null=True,blank=True)
    sale_account = models.CharField(max_length=30,null=True,blank=True)
    sale_desc = models.CharField(max_length=30,null=True,blank=True)
    tax = models.CharField(max_length=30,null=True,blank=True)
    purchase_price = models.CharField(max_length=30,null=True,blank=True)
    purchase_account = models.CharField(max_length=30,null=True,blank=True)
    purchase_desc = models.CharField(max_length=30,null=True,blank=True)
    inv_account = models.CharField(max_length=30,null=True,blank=True)
    inv_reorder_level = models.CharField(max_length=30,null=True,blank=True)
    inv_opening_stock = models.CharField(max_length=30,null=True,blank=True)
    inv_opening_stock_value = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.item_name

class ItemGroup(models.Model):
    item_group_id = models.CharField(max_length=30,null=True,blank=True)
    item_group_name = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.item_group_name        

class SalesOrder(models.Model):
    so_number = models.CharField(max_length=30,null=True,blank=True)
    so_customer = models.CharField(max_length=30,null=True,blank=True)
    so_reference = models.CharField(max_length=30,null=True,blank=True)
    so_date = models.CharField(max_length=30,null=True,blank=True)
    so_amount = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.so_number

class SalesOrderItem(models.Model):
    so_number = models.CharField(max_length=30,null=True,blank=True)
    so_item_id = models.CharField(max_length=30,null=True,blank=True)
    so_item_qty = models.CharField(max_length=30,null=True,blank=True)
    so_item_rate = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.so_number      

class DeliveryOrder(models.Model):
    do_number = models.CharField(max_length=30,null=True,blank=True)
    do_customer = models.CharField(max_length=30,null=True,blank=True)
    do_reference = models.CharField(max_length=30,null=True,blank=True)
    do_date = models.CharField(max_length=30,null=True,blank=True)
    do_qty_total = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.do_number 

class DeliveryOrderItem(models.Model):
    do_number = models.CharField(max_length=30,null=True,blank=True)
    do_item_id = models.CharField(max_length=30,null=True,blank=True)
    do_item_qty = models.CharField(max_length=30,null=True,blank=True)
    do_item_rate = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.do_number   


    