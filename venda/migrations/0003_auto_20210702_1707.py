# Generated by Django 3.1.2 on 2021-07-02 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('venda', '0002_auto_20210702_1643'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemCarrinho',
            new_name='Item',
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Item', 'verbose_name_plural': 'Intens'},
        ),
    ]
