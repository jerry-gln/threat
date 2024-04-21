# Generated by Django 5.0.3 on 2024-03-31 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_supplier_alter_order_is_auto_generated'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.supplier'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='supplier',
            field=models.CharField(choices=[('Total Gas', 'Total Gas'), ('Iron Sheets', 'Sheets')], max_length=200, null=True),
        ),
    ]
