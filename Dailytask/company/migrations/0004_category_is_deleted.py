# Generated by Django 3.1.7 on 2021-09-08 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_product_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted'),
        ),
    ]
