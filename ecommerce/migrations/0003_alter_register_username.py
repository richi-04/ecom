# Generated by Django 4.0.4 on 2022-05-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_remove_register_pswd2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
