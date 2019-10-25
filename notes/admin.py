from django.contrib import admin
from notes.models import Notes, NotesItem


# Register your models here.
class NotesItemInline(admin.TabularInline):  
    model = NotesItem
    extra = 3

class NotesAdmin(admin.ModelAdmin):
    list_display = NotesItem (
      'title',
      'item_count',
      'update_at',
    )  
    inlines = [NotesItemInline]



admin.site.register(Notes, NotesAdmin)
admin.site.register(NotesItem)

