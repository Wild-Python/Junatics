# Generated by Django 5.0.3 on 2024-03-16 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Junatics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='product_images/')),
                ('is_favorite', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Junatics',
            },
        ),
    ]