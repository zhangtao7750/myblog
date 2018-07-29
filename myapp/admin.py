from django.contrib import admin
from .models import PostB737,PostFlight

# Register your models here.
class PostFlightAdmin(admin.ModelAdmin):
    list_display = ['title','title_auther','title_num','title_date']
    list_filter = ['title']
    list_per_page = 10
    search_fields =  ['title','title_auther','title_num','title_date']

admin.site.register(PostFlight,PostFlightAdmin)

class PostB737Admin(admin.ModelAdmin):
    list_display = ['title','title_auther','title_num','title_date']
    list_filter = ['title']
    list_per_page = 10
    search_fields =  ['title','title_auther','title_num','title_date']

admin.site.register(PostB737,PostB737Admin)