from django.contrib import admin
from .models import Register,Contact,Reviews,demo
# Register your models here.

admin.site.register(Register)
admin.site.register(Contact)
admin.site.register(Reviews)

admin.site.register(demo)