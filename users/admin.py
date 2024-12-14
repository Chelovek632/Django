from django.contrib import admin

# Register your models here.

from carts.models import Cart
from orders.admin import OrderTabulareAdmin
from users.models import User

admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [OrderTabulareAdmin]