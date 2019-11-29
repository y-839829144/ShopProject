# Generated by Django 2.2.6 on 2019-10-16 04:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女'), (3, '保密')], verbose_name='用户性别')),
                ('picture', models.ImageField(upload_to='uploads/user/%Y/', verbose_name='用户头像')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShopAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='收货人姓名')),
                ('tel', models.CharField(max_length=20, verbose_name='联系方式')),
                ('address', models.CharField(max_length=255, verbose_name='收货地址')),
                ('zipcode', models.IntegerField(verbose_name='邮编')),
                ('is_default', models.BooleanField(default=False, verbose_name='是否默认')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '收货地址',
            },
        ),
    ]