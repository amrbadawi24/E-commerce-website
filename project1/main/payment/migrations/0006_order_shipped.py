# Generated by Django 5.0.6 on 2024-07-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_alter_order_item_order_alter_order_item_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
    ]
