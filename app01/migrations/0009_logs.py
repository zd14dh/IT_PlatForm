# Generated by Django 3.2 on 2022-11-04 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20221101_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_report', models.TextField(default='', verbose_name='报告')),
                ('log_run_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='log日志产生时间')),
                ('log_pass_count', models.IntegerField(verbose_name='通过数量')),
                ('log_failed_count', models.IntegerField(verbose_name='失败数量')),
                ('log_run_count', models.IntegerField(verbose_name='执行用例总数量')),
                ('log_sub_it', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.it', verbose_name='所属接口的项目')),
            ],
        ),
    ]