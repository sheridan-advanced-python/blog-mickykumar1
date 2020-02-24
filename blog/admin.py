
# blog/admin.py
from django.contrib import admin
from . import models

# Register the `Post` model
class PostAdmin(admin.ModelAdmin):
    """customising post model view"""
    list_display = ('title', 'author', 'created', 'updated')
    #The list display should be customized
    search_fields = ('title', 'author__username', 'author__first_name', 'author__last_name')
    #The comment list should be searchable
    #list_filter = (status)

    def author(self, obj):#for list_display author
        return obj.author

    def title(self, obj):#for list_display title
        return obj.title

    def status(self, obj):
        return obj.status

# Register the `Post` model
admin.site.register(models.Post, PostAdmin)
# Register the `Comment` model
admin.site.register(models.Comment, PostAdmin)
