# Generated by Django 5.0 on 2023-12-20 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_date_added_alter_book_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 20, 18, 46, 1, 495988)),
        ),
    ]
