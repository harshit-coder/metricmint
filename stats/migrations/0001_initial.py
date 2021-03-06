# Generated by Django 3.0 on 2020-12-17 05:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import stats.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='ALL', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='codes_list',
            fields=[
                ('co', models.CharField(max_length=900, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(default='ALL', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searc', models.CharField(max_length=1000, null=True)),
                ('d', models.DateTimeField(default=datetime.datetime(2020, 12, 17, 5, 59, 22, 486278, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_subcategory', models.CharField(blank=True, max_length=100, null=True)),
                ('graph', models.CharField(blank=True, choices=[('bar', 'bar'), ('pie', 'pie'), ('scatter', 'scatter'), ('cylinder', 'cylinder'), ('funnel3d', 'funnel3d'), ('pyramid3d', 'pyramid3d'), ('gauge', 'gauge'), ('area', 'area'), ('areaspline', 'areaspline'), ('bullet', 'bullet'), ('column', 'column'), ('columnpyramid', 'columnpyramid'), ('dependencywheel', 'dependencywheel'), ('dumbbell', 'dumbbell'), ('heatmap', 'heatmap'), ('histogram', 'histogram'), ('item', 'item'), ('line', 'line'), ('lollipop', 'lollipop'), ('networkgraph', 'networkgraph'), ('packedbubble', 'packedbubble'), ('spline', 'spline'), ('wordcloud', 'wordcloud'), ('columnrange', 'columnrange'), ('spline', 'spline'), ('streamgraph', 'streamgraph'), ('sunburst', 'sunburst'), ('tilemap', 'tilemap'), ('timeline', 'timeline'), ('treemap', 'treemap'), ('variablepie', 'variablepie'), ('variwide', 'variwide'), ('vector', 'vector'), ('venn', 'venn'), ('xrange', 'xrange')], default='bar', max_length=100)),
                ('graph_tittle', models.CharField(blank=True, max_length=100, null=True)),
                ('x_axistittle', models.CharField(blank=True, max_length=100, null=True)),
                ('y_axistittle', models.CharField(blank=True, max_length=100, null=True)),
                ('s_csv', models.FileField(null=True, upload_to='files/')),
                ('s_head_tittle', models.CharField(blank=True, max_length=50, null=True)),
                ('s_head_subtittle', models.CharField(blank=True, max_length=100, null=True)),
                ('s_date', models.DateField(default=datetime.datetime(2020, 12, 17, 5, 59, 22, 486278, tzinfo=utc))),
                ('s_publisher', models.CharField(blank=True, max_length=100, null=True)),
                ('s_src1', models.URLField(blank=True)),
                ('desc1', models.TextField(blank=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('x_pts', models.TextField(blank=True, null=True)),
                ('y_pts', models.TextField(blank=True, null=True)),
                ('s_Category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stats.cat')),
                ('s_count', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.country')),
            ],
        ),
        migrations.CreateModel(
            name='search1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searches', models.CharField(max_length=1000, null=True)),
                ('c_ategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.cat')),
                ('c_ountry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.country')),
            ],
        ),
        migrations.CreateModel(
            name='Multiple_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=stats.models.path_and_rename)),
                ('date_inp', models.DateTimeField(default=datetime.datetime(2020, 12, 17, 5, 59, 22, 486278, tzinfo=utc))),
                ('code', models.ForeignKey(db_column='co', null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.codes_list')),
            ],
        ),
        migrations.CreateModel(
            name='infog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_subcategory', models.CharField(blank=True, max_length=100)),
                ('image_tittle', models.CharField(blank=True, max_length=100, null=True)),
                ('imageurl1', models.URLField(blank=True, null=True)),
                ('i_head_tittle', models.CharField(blank=True, max_length=100)),
                ('i_sub_tittle', models.CharField(blank=True, max_length=100)),
                ('i_publisher', models.CharField(default='Ankit Kalucha', max_length=100)),
                ('i_date', models.DateField(default=datetime.datetime(2020, 12, 17, 5, 59, 22, 486278, tzinfo=utc))),
                ('i_image', models.ImageField(upload_to='images/')),
                ('i_src1', models.URLField(blank=True)),
                ('image2field', models.FilePathField(max_length=200, null=True, path='E:\\metricmint\\media\\images', recursive=True)),
                ('desc2', models.TextField(blank=True)),
                ('i_category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stats.cat')),
                ('i_count', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stats.country')),
            ],
        ),
    ]
