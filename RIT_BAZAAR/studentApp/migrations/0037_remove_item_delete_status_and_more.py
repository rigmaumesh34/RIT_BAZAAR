# Generated by Django 5.1 on 2024-09-03 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0036_item_delete_status_student_delete_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='delete_status',
        ),
        migrations.RemoveField(
            model_name='student',
            name='delete_status',
        ),
    ]
