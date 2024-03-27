from django.db import models


def user_directory_path(instance, filename):
    return f'product_images/{instance.id}/{filename}'


class JunaticsManager(models.Manager):
    def get_queryset(self):
        return super(JunaticsManager, self).get_queryset().filter(is_active=True)


class Junatics(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to=user_directory_path,
                              verbose_name='Product Image:',
                              blank=True, null=True)
    is_favorite = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # Custom Manager
    objects = models.Manager()
    junatics = JunaticsManager()

    class Meta:
        verbose_name = 'Junatics'
        verbose_name_plural = 'Junatics'

    def __str__(self):
        return self.name
