# Generated by Django 4.1.3 on 2022-12-13 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0007_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
