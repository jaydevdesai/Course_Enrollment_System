# Generated by Django 3.1.2 on 2020-11-30 00:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0006_auto_20201122_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Order Date',
        ),
    ]
