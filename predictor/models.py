from django.db import models

# Create your models here.
class Kitabs(models.Model):
    no_database = models.IntegerField()
    kategori = models.CharField(max_length=100)
    nama_kitab = models.CharField(max_length=1000)
    pengarang = models.CharField(max_length=1000)
    no_halaman = models.TextField()
    teks_processing = models.TextField()

    def __str__(self):
        return "{}".format(self.no_database)