# Generated by Django 3.0.3 on 2020-02-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0002_auto_20200204_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='t_type',
            field=models.CharField(default='test', max_length=10),
            preserve_default=False,
        ),
    ]
