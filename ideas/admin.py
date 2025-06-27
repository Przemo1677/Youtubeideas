from django.contrib import admin
from .models import Idea, Vote
from django.utils.html import format_html



# Register your models here.

class VoteInline(admin.StackedInline):
    model = Vote
    


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'status', 'youtube_url']
    list_filter = ['status']
    inlines = [
        VoteInline
    ]
    
    def show_youtube_url(self, obj):
        if obj.youtube_url is not None:
            return format_html(f'<a href="{obj.youtube_url}" target="_blank">{obj.youtube_url}</a>')
        else:
            return ''
        
    show_youtube_url.short_description = 'Youtube url'
    

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id','idea','reason']
    list_filter = ['idea']

