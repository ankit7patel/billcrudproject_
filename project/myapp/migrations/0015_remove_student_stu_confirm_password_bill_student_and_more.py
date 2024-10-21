# Generated by Django 5.1.2 on 2024-10-17 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_bill_student_student_stu_confirm_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='stu_confirm_password',
        ),
        migrations.AddField(
            model_name='bill',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bill',
            name='item_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_password',
            field=models.CharField(max_length=100),
        ),
    ]
