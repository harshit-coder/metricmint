# Generated by Django 3.0 on 2020-12-17 16:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0008_auto_20201217_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infog',
            name='i_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 17, 16, 59, 3, 854367, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='multiple_images',
            name='date_inp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 16, 59, 3, 855355, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='searchenter',
            name='d',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 16, 59, 3, 855355, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='stat',
            name='s_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 17, 16, 59, 3, 853315, tzinfo=utc)),
        ),
    ]
