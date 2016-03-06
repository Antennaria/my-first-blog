from django.contrib import admin
from .models import Post

admin.site.register(Post) #регистрируем созданную нами модель, чтобы она была доступна для администрирования

# Register your models here.
