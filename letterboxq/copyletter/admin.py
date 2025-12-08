from django.contrib import admin

# Register your models here.
# username = yusuf
# mail yusuf@gmail.com
# password = Yusuf1234.

from django.contrib import admin
from .models import Movies

admin.site.register(Movies)