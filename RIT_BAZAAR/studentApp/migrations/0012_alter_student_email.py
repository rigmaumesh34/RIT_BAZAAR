# Generated by Django 5.1 on 2024-08-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0011_remove_student_created_at_remove_student_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
