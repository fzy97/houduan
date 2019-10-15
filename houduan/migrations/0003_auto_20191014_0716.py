# Generated by Django 2.2.6 on 2019-10-14 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houduan', '0002_listings'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='name',
            field=models.CharField(default='no', max_length=100, verbose_name='name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listings',
            name='neighbourhood_group_cleansed',
            field=models.CharField(default='no', max_length=100, verbose_name='neighbourhood_group_cleansed'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listings',
            name='price',
            field=models.CharField(default='not_clear', max_length=100, verbose_name='price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listings',
            name='review_scores_rating',
            field=models.CharField(default='no', max_length=100, verbose_name='review_scores_rating'),
            preserve_default=False,
        ),
    ]