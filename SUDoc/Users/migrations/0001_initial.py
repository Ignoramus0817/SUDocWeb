# Generated by Django 2.1.5 on 2019-01-29 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentID', models.CharField(default='PB00000000', max_length=10, unique=True, verbose_name='学号')),
                ('userName', models.CharField(max_length=20, unique=True, verbose_name='姓名')),
                ('passWord', models.CharField(max_length=30, verbose_name='密码')),
                ('email_Address', models.EmailField(max_length=254, unique=True, verbose_name='邮箱地址')),
            ],
        ),
    ]
