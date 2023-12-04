from django.contrib import admin

from home.models import Comment, ContactFormMessage, ReplyComment, Setting, UserProfile


# Register your models here.

admin.site.register(Setting)

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject','update_at','status'] #! görüntülenecek kısım.
    readonly_fields = ('name','subject','email','message','ip') #! düzenleme yapılamayacak olanlar.
    list_filter = ['status']
    #! fields = ['name','subject'] # sadece bu kısımlar görünür.
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','subject','comment','status','create_at']
    list_filter = ['status']
    readonly_fields = ('subject','comment','ip','user','id')
admin.site.register(Comment, CommentAdmin)

class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ['user','subject','repcomment','status','create_at']
    list_filter = ['status']
    readonly_fields = ('subject','repcomment','ip','user','id')

admin.site.register(ReplyComment, ReplyCommentAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address', 'phone','city','country','image_tag']

admin.site.register(UserProfile, UserProfileAdmin)