from django.contrib import admin
from .models import *
from .models import Biodata

# Register your models here

class BioadataAdmin(admin.ModelAdmin):
    list_display =('user','alamat','telp')
admin.site.register(Biodata, BioadataAdmin)

class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('nama', 'judul', 'body', 'kategory', 'date')

admin.site.register(Kategori)
admin.site.register(Artikel, ArtikelAdmin)

class APIadmin(admin.ModelAdmin):
    list_display = ('user', 'api_key')
admin.site.register(API, APIadmin)