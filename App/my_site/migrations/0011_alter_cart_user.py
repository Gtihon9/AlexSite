# Generated by Django 4.1.3 on 2023-01-02 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0010_alter_cart_total_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]