from django.db import models


def user_directory_path(instance, filename):
    return f'product_images/{instance.id}/{filename}'


class Junatics(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to=user_directory_path,
                              verbose_name='Product Image:',
                              blank=True, null=True)
    is_favorite = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Junatics'

    def __str__(self):
        return self.name
