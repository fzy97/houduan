# Generated by Django 2.2.6 on 2019-10-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houduan', '0004_auto_20191014_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='avaliability_365',
        ),
        migrations.AddField(
            model_name='listings',
            name='availability_365',
            field=models.CharField(default=0, max_length=100, verbose_name='availability_365'),
            preserve_default=False,
        ),
    ]
