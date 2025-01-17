# Generated by Django 5.1.2 on 2024-10-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_student_stu_confirm_password_bill_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='student',
        ),
        migrations.AddField(
            model_name='student',
            name='stu_confirm_password',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_email',
            field=models.EmailField(max_length=254),
        ),
    ]
