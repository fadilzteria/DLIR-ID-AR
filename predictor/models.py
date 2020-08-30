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
        return "{}. {} {}".format(self.id, self.nama_kitab, self.no_halaman)
    
class Review(models.Model):
    username = models.CharField(max_length=100)
    query = models.CharField(max_length=100)
    review = models.CharField(max_length=500)

    CHOICE = [('Iya', 'Iya'), ('Tidak', 'Tidak')]

    dokumen_relevan = models.IntegerField(default=0)
    konfirmasi = models.BooleanField(default=False)

    def __str__(self):
        return "{}. {}".format(self.id, self.query)