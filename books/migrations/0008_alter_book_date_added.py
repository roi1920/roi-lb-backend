# Generated by Django 5.0 on 2023-12-24 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_borrowers_alter_book_date_added_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 24, 15, 13, 55, 231909)),
        ),
    ]
