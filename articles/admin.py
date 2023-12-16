from django.contrib import admin

from articles.models import Article, Comments

# Register your models here.


class CommentsInLine(admin.TabularInline):
    model = Comments


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentsInLine
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comments)
