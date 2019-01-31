from django.db import models

# Create your models here.
class User(models.Model):
    studentID = models.CharField(max_length = 10, unique = True, verbose_name = '学号', default = 'PB00000000')
    userName = models.CharField(max_length = 20, unique = True, verbose_name = '姓名')
    passWord = models.CharField(max_length = 30, verbose_name = '密码')
    email_Address = models.EmailField(max_length = 254, unique = True, verbose_name = '邮箱地址')