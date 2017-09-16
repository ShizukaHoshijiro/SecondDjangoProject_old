from django.contrib import admin
from .models import Article, Comment

# admin.site.register(Article)

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

admin.site.register(Article, ArticleAdmin)
