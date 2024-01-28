from django.contrib import admin
from .models import CustomUser,Dashboard,Sponsors

admin.site.register(CustomUser)
admin.site.register(Dashboard)
admin.site.register(Sponsors)