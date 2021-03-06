# Generated by Django 3.1.4 on 2020-12-10 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Categories name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m', verbose_name='Photo')),
                ('description', models.TextField(max_length=320, verbose_name='Description')),
                ('price', models.IntegerField()),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='Publication date')),
                ('is_published', models.BooleanField(default=True, verbose_name='Published')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='onlinecatalog.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-pub_date'],
            },
        ),
    ]
