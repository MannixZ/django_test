# Generated by Django 2.2.5 on 2019-12-29 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0010_auto_20191229_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(default='', max_length=30, verbose_name='老师')),
                ('tel', models.CharField(default='', max_length=30, verbose_name='电话')),
                ('mail', models.CharField(default='', max_length=30, verbose_name='邮箱')),
            ],
            options={
                'verbose_name': '老师',
                'verbose_name_plural': '老师',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(default='', max_length=30, verbose_name='学号')),
                ('name', models.CharField(default='', max_length=30, verbose_name='姓名')),
                ('age', models.IntegerField(default='', verbose_name='年龄')),
                ('teachers', models.ManyToManyField(to='hello.Teacher', verbose_name='老师')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
        ),
    ]