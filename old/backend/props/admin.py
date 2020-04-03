from django.contrib import admin
from grappelli_modeltranslation.admin import TranslationAdmin
from .models import *
from account.admin import superadmin_site



class ValueInline(admin.StackedInline):
    model = Value
    list_editable = ['title']

from .models import *
# Register your models here.
@admin.register(Props, site=superadmin_site)
class PropsAdmin(TranslationAdmin):
    list_display = ['name', 'icon_img', 'alias', 'type', 'for_man', 'for_woman']
    inlines = [ValueInline]
  

class ValueAdmin(TranslationAdmin):
    list_display = ['name_ru', 'name_en', 'prop']
admin.site.register(Value, ValueAdmin)

class Value2UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(Value2User, Value2UserAdmin)