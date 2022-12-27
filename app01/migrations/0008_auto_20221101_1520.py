# Generated by Django 3.2 on 2022-11-01 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_alter_api_api_run_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='api_data',
            field=models.CharField(default={}, max_length=255, verbose_name='请求的data'),
        ),
        migrations.AlterField(
            model_name='api',
            name='api_desc',
            field=models.CharField(default='', max_length=255, verbose_name='用例描述'),
        ),
        migrations.AlterField(
            model_name='api',
            name='api_exprct',
            field=models.CharField(default={}, max_length=4196, verbose_name='预期结果'),
        ),
        migrations.AlterField(
            model_name='api',
            name='api_params',
            field=models.CharField(default={}, max_length=255, verbose_name='请求的参数'),
        ),
        migrations.AlterField(
            model_name='api',
            name='api_report',
            field=models.TextField(default='', verbose_name='报告'),
        ),
        migrations.AlterField(
            model_name='api',
            name='api_url',
            field=models.CharField(default='', max_length=255, verbose_name='请求的url'),
        ),
    ]
