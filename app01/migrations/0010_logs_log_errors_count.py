# Generated by Django 3.2 on 2022-11-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_logs'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='log_errors_count',
            field=models.IntegerField(default=1, verbose_name='报错数量'),
            preserve_default=False,
        ),
    ]
