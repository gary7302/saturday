# Generated by Django 4.1.7 on 2023-04-12 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_spanishcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
