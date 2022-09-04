from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name
