from django.contrib import admin
from product.models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'comment', 'status','create_at']
    list_filter = ['status']

admin.site.register(Comment, CommentAdmin)