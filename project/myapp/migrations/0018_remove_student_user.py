# Generated by Django 5.1.2 on 2024-10-17 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_bill_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
    ]