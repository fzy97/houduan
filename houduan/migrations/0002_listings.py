# Generated by Django 2.2.6 on 2019-10-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houduan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_url', models.CharField(max_length=200, verbose_name='listing_url')),
                ('picture_url', models.CharField(max_length=200, verbose_name='picture_url')),
            ],
            options={
                'verbose_name': 'listing',
                'verbose_name_plural': 'listing',
                'db_table': 'listings',
            },
        ),
    ]