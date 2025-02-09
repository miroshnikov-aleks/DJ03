from django.contrib import admin
from .models import News_post

@admin.register(News_post)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'user_name')
    search_fields = ('title', 'user_name')