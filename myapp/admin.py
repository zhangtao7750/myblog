from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','title_auther','title_num','title_date']
    list_filter = ['title']
    list_per_page = 10
    search_fields =  ['title','title_auther','title_num','title_date']

admin.site.register(Post,PostAdmin)
