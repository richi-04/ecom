# Generated by Django 4.0.4 on 2022-05-25 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_customer_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='product',
        ),
    ]