# Generated by Django 4.1.1 on 2022-09-29 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                default=models.CharField(max_length=20), unique=True
            ),
        ),
    ]
