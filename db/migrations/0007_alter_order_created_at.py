# Generated by Django 4.0.2 on 2023-03-27 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_alter_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
