# Generated by Django 5.1 on 2024-09-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0032_events'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
