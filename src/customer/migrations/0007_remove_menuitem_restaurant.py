# Generated by Django 4.1 on 2023-05-29 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_alter_menuitem_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='restaurant',
        ),
    ]
