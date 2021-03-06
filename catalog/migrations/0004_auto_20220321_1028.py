# Generated by Django 3.2.12 on 2022-03-21 10:28

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_item_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликованно')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
                ('weight', models.IntegerField(default=100, validators=[django.core.validators.MaxValueValidator(32767)], verbose_name='Вес')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.category', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
