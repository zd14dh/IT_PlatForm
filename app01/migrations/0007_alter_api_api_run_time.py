# Generated by Django 3.2 on 2022-10-31 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20221031_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='api_run_time',
            field=models.DateTimeField(null=True, verbose_name='执行时间'),
        ),
    ]
