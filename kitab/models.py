from django.db import models

# Create your models here.
class UploadKitab(models.Model):
    kategori = models.CharField(max_length=100)
    nama_kitab = models.CharField(max_length=100)
    nama_pengarang = models.CharField(max_length=1000)
    file_kitab = models.FileField()

    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama_kitab)
