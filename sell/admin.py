from django.contrib import admin

# Register your models here.
from .models import Writing
from .models import Category, Comment, Ip
from .models import User
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

    list_display = ('subject', 'author', 'content', 'create_date')
admin.site.register(Writing, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'deleted')
    search_fields = ['content']
admin.site.register(Comment, CommentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'description')
admin.site.register(Category, CategoryAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','level', 'date_joined')
admin.site.register(User, UserAdmin)

class IpAdmin(admin.ModelAdmin):
  list_display = ('user', 'ip')
  search_fields = ['user__username','ip']
admin.site.register(Ip, IpAdmin)