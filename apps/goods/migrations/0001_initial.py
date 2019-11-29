# Generated by Django 2.2.6 on 2019-10-16 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='商品名称')),
                ('original_price', models.FloatField(verbose_name='原价')),
                ('actual_price', models.FloatField(verbose_name='现价')),
                ('freight', models.FloatField(verbose_name='运费')),
                ('image', models.ImageField(upload_to='uploads/goods/%Y/%m/%d/', verbose_name='商品图片')),
                ('detail', models.CharField(max_length=255, verbose_name='说明')),
                ('sale_nums', models.IntegerField(verbose_name='销量')),
                ('all_nums', models.IntegerField(verbose_name='库存')),
                ('view_nums', models.IntegerField(verbose_name='浏览量')),
                ('favor_nums', models.IntegerField(verbose_name='收藏量')),
                ('comments_nums', models.IntegerField(verbose_name='评论数')),
                ('created_time', models.DateTimeField(verbose_name='录入时间')),
            ],
            options={
                'verbose_name': '商品信息表',
            },
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='分类名称')),
                ('level', models.IntegerField(verbose_name='分类级别')),
                ('uper_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsType', verbose_name='上级编号')),
            ],
            options={
                'verbose_name': '商品信息分类表',
            },
        ),
        migrations.CreateModel(
            name='GoodsDisplayFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='说明')),
                ('goods_file', models.FileField(upload_to='upload/goods/%Y/%m/%d/', verbose_name='展示图')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
            ],
            options={
                'verbose_name': '商品展示文件信息表',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='one_typename',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='one', to='goods.GoodsType'),
        ),
        migrations.AddField(
            model_name='goods',
            name='three_typename',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='three', to='goods.GoodsType'),
        ),
        migrations.AddField(
            model_name='goods',
            name='two_typename',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='two', to='goods.GoodsType'),
        ),
    ]
