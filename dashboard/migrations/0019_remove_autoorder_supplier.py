# Generated by Django 5.0.4 on 2024-04-14 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_autoorder_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoorder',
            name='supplier',
        ),
    ]
