# Generated by Django 4.1.5 on 2023-01-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_views', '0003_alter_author_salutation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='state_province',
            field=models.CharField(max_length=30, verbose_name='Provincia'),
        ),
    ]
