# Generated by Django 5.1.2 on 2024-10-16 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_bill_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='user',
        ),
    ]
