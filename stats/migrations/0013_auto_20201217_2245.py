# Generated by Django 3.0 on 2020-12-17 17:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0012_auto_20201217_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codes_list',
            name='co',
            field=models.CharField(max_length=900, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='infog',
            name='i_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 17, 17, 15, 20, 413976, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='multiple_images',
            name='date_inp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 17, 15, 20, 413976, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='searchenter',
            name='d',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 17, 15, 20, 413976, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='stat',
            name='s_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 17, 17, 15, 20, 413976, tzinfo=utc)),
        ),
    ]
