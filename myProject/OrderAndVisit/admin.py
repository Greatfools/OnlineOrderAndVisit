from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Hospital)
admin.site.register(User)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(VisitMessage)
admin.site.register(OrderMessage)
admin.site.register(RegisterMessage)
admin.site.register(OrderCancelMessage)
admin.site.register(PayMessage)