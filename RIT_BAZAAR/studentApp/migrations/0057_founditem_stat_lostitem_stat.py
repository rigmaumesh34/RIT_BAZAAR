# Generated by Django 5.1 on 2024-10-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0056_item_paid_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='founditem',
            name='stat',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
        migrations.AddField(
            model_name='lostitem',
            name='stat',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]
