# Generated by Django 4.1.3 on 2022-12-13 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0005_alter_entry_product_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_site.product'),
        ),
    ]