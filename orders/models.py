from django.db import models
from django.conf import settings
from accounts.models import Address
from django.core.validators import MinValueValidator,MaxValueValidator
from products.models import Product
from layout.utils import jalali_converter
#---------------------------
def format(show):
    formatted_price = "{:,.0f}".format(show)
    return formatted_price
#---------------------------
class BankAccount(models.Model):
    number = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=20)
    owner = models.CharField(max_length=20)

    def __str__(self):
        return str(self.number) + str(self.bank_name)
#---------------------------
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    discount = models.IntegerField(blank=True,null=True,default=None)
    recipient = models.CharField(max_length=100)
    

    ref_id = models.CharField(max_length=100,blank=True,null=True,default=None)
    authority = models.CharField(max_length=100,blank=True,null=True,default=None)

    address = models.ForeignKey(Address,on_delete=models.CASCADE,blank=True,null=True,default=None)
    

    processed = models.BooleanField(default=False)
    packing = models.BooleanField(default=False) 
    shipped = models.BooleanField(default=False)
    deliveried = models.BooleanField(default=False) 
    returned = models.BooleanField(default=False)



    class Meta:
        ordering = ('-created',)
    
    def paid_string(self):
        if self.paid:
            return f"پرداخت شده."
        return f"پرداخت نشده."
    
    @property
    def discount_string(self):
        if self.discount == None:
            return f" تخفیفی اعمال نشده است."
        return f"{self.discount} درصد تخفیف اعمال شده است"

    @property
    def discount_amount(self):
        if self.discount == None:
            return f" تخفیفی اعمال نشده است."
        return self.discount * self.total_price / 100

    @property
    def pay_amount(self):
        return self.total_price - self.discount_amount

    def __str__(self):
        return f'{self.user} - {self.id}'

    def formatPay(self,pay):
        return "{:,.0f}".format(pay)

    @property
    def total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price = (self.discount/100)* total
            return total - discount_price
        return total

    def tax(self):
        return 9 * self.total_price() / 100
    
    def get_tax(self):
        return "{:,.0f}".format(9 * self.total_price() / 100)

    def taxAndTotal(self):
        return "{:,.0f}".format(self.total_price() + self.tax())

    @property
    def shamsi_date(self):
        return jalali_converter(self.created)

    def get_order_number(self):
        order_id = self.id
        order_num = abs(hash(self.created)) % (10 ** 5)
        order_num_str = str(order_num).zfill(5)
        return order_num_str
#---------------------------
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_items')
    price = models.IntegerField()
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.id}-{self.product}"


    def get_cost(self):
        return self.product.discounted_price_int * self.quantity

    def get_cost_from_product(self):
        return format(self.product.discounted_price_int * self.quantity)
#---------------------------


