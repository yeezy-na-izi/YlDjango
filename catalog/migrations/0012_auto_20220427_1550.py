# Generated by Django 3.2.12 on 2022-04-27 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_item_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Gallery',
            new_name='Image',
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
    ]
