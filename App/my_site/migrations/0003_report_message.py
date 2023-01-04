# Generated by Django 4.1.3 on 2022-11-28 13:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
