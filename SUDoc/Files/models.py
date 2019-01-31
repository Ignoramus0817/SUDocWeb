from django.db import models

# Create your models here.

class File(models.Model):
    dynamicPath  = 'documents/upload/'
    fileName = models.CharField(max_length = 30, unique = True, verbose_name = '文件名')
    createDate = models.DateField(unique = True, verbose_name = '创建日期')
    filePath = models.FileField(upload_to = dynamicPath, verbose_name = '文件路径')
    uploader = models.CharField(max_length = 30, unique = True, '上传者')
    