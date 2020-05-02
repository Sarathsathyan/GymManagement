from django.contrib import admin
from .models import Contact,Reviews,demo,UserDetails,Courses,Register,customer,payments,transformation
# Register your models here.


admin.site.register(Contact)
admin.site.register(Reviews)

admin.site.register(demo)
admin.site.register(UserDetails)
admin.site.register(Courses)
admin.site.register(Register)
admin.site.register(customer)
admin.site.register(payments)
admin.site.register(transformation)