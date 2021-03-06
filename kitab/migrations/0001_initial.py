# Generated by Django 3.0.3 on 2020-07-20 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadKitab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori', models.CharField(max_length=100)),
                ('nama_kitab', models.CharField(max_length=100)),
                ('nama_pengarang', models.CharField(max_length=1000)),
                ('file_kitab', models.FileField(upload_to='')),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
