# Generated by Django 5.1 on 2024-09-03 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0039_alter_item_delete_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='delete_status',
            field=models.CharField(choices=[(1, 'Live'), (0, 'Delete')], default=1),
        ),
    ]
