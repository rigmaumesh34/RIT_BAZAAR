# Generated by Django 5.1 on 2024-09-03 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0034_alter_founditem_student_alter_student_password'),
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
