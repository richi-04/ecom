# Generated by Django 4.0.4 on 2022-06-01 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_alter_cart_amt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='amt',
        ),
        migrations.AddField(
            model_name='check_pdtl',
            name='amt',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
