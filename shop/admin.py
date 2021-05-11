from django.contrib import admin
from .models import product,Contact,Orders,orderupdate,Blog

# Register your models here.
admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(orderupdate)
admin.site.register(Blog)

