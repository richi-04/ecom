# Generated by Django 4.0.4 on 2022-06-01 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_rename_productname_check_pdtl_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('customer_email', models.EmailField(max_length=254, verbose_name='Customer Email')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('stripe_payment_intent', models.CharField(max_length=200)),
                ('has_paid', models.BooleanField(default=False, verbose_name='Payment Status')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.cart', verbose_name='Product')),
            ],
        ),
    ]
