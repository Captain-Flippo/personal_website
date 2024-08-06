from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from blog.models import Category, Comment, Post


class CategoryAdmin(admin.ModelAdmin):
    pass


# class PostAdmin(admin.ModelAdmin):
#     pass


class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class BlogPostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'created_on', 'last_modified')
    search_fields = ('title', 'categories')

admin.site.register(Category, CategoryAdmin)
#admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
#admin.site.register(Post, MarkdownxModelAdmin)