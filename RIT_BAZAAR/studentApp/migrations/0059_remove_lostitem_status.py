# Generated by Django 5.1 on 2024-10-04 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0058_remove_founditem_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lostitem',
            name='status',
        ),
    ]
