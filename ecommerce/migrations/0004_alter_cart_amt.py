# Generated by Django 4.0.4 on 2022-05-31 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_cart_amt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='amt',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
