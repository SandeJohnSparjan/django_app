from django.contrib import admin
from home.models import Post,Friend
# Register your models here.

#friendlist functionality
admin.site.register(Friend)
admin.site.register(Post)