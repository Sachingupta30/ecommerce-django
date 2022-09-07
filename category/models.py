from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    categoy_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)  #for url
    description = models.TextField(max_length=250, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

# below meta code is for typothing of modal name...
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.categoy_name