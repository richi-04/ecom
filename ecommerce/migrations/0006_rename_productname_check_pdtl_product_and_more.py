# Generated by Django 4.0.4 on 2022-06-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_remove_cart_amt_check_pdtl_amt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='check_pdtl',
            old_name='productname',
            new_name='product',
        ),
        migrations.AddField(
            model_name='check_pdtl',
            name='stripe_amt',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stripe_product_id',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]