from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

#mengambil tabel user
class Biodata(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField() 
    telp = models.CharField(max_length=14)

    def __str__(self):
        return "{} - {}".format (self.user, self.telp) 


class API(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Kategori(models.Model):
    nama = models.CharField(max_length=20)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural ="Kategori"

class Artikel(models.Model):
    nama = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    judul = models.CharField(max_length=100)
    body = RichTextUploadingField(blank=True, null=True,
                                    config_name='special',
                                    external_plugin_resources=[(
                                        'youtube',
                                        '/static/ckeditor_plugins/youtube/youtube/',
                                        'plugin.js',
                                        )],
)
    kategory = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{} - {}".format(self.nama, self.judul)

    class Meta:
        ordering =['-date']
        verbose_name_plural ="Artikel"
