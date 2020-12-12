from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Photo')
    description = models.TextField(max_length=320, verbose_name='Description')
    price = models.IntegerField()
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Publication date')
    gi = models.BooleanField(default=True, verbose_name='Published')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-pub_date']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Categories name')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']
