#make migrations every time you change models.py file

from django.contrib import admin
#importing UserProfile model form models.py
from accounts.models import UserProfile

# Register your models here.

#creating admin
#UserProfile is the name of the model in models.py
#this will create a folder in admin db


#admin.site.site_header = 'Administration'


#adding a column in django admin page
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_info', 'city','phone', 'website')

    #adding a column name user_info
    def user_info(self, obj):
        return obj.description

    #to change the name of the column
    user_info.short_description ='Info'

    #changing the order by changing the queryset(list) in UserProfileAdmin
    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user')
        return queryset


admin.site.register(UserProfile, UserProfileAdmin)