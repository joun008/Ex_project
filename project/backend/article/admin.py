from django.contrib import admin
from .models import Article, User_Article_match, Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('postDate', 'writerID')
    readonly_fields = ('hits','postDate', 'modifiedDate')
    fieldsets = (
        (None, {
            'fields': ('writerID', 'lab', 'title', ('postDate', 'modifiedDate'), ('startDay', 'endDay'), ('startBirth', 'endBirth'))
        }),
        ('keywords', {
            'fields': ('gender', 'isOffline', 'reward', 'location', 'subject')
        }),
        ('etc', {
            'fields': ('content', 'articleFile', 'articleImg', 'hits')
        })
    )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(User_Article_match)

# Register your models here.
