# Generated by Django 5.1.2 on 2024-10-17 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_remove_bill_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
