from django.contrib import admin
from .models import userlog
from .models import user
from .models import userbill
# Register your models here.
admin.site.register(userlog)
admin.site.register(user)
admin.site.register(userbill)