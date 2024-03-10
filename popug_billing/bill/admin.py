from django.contrib import admin

from .models import BillingCycle, CustomUser, Task, Transaction

admin.site.register(CustomUser)
admin.site.register(Task)
admin.site.register(BillingCycle)
admin.site.register(Transaction)
