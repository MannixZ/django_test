# Generated by Django 2.2.5 on 2019-12-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_bank_cardinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auther',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='作者')),
                ('mail', models.CharField(max_length=30, verbose_name='邮箱')),
                ('city', models.CharField(max_length=10, verbose_name='城市')),
            ],
            options={
                'verbose_name_plural': '作者',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50, verbose_name='书名')),
                ('auth', models.ManyToManyField(to='hello.Auther', verbose_name='作者')),
            ],
            options={
                'verbose_name_plural': '书籍详情',
            },
        ),
    ]