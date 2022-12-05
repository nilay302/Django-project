from django.contrib import admin
from . import models
# Register your models here.
class TweetsAdmin(admin.ModelAdmin):
    list_display = ('title',)#To show the title name in admin site

admin.site.register(models.Tweets,TweetsAdmin)