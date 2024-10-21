# Generated by Django 5.1.2 on 2024-10-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_bill_item_name_alter_bill_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='user',
        ),
        migrations.AlterField(
            model_name='bill',
            name='price_per_item',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
