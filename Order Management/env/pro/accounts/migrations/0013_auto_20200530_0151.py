# Generated by Django 3.0.6 on 2020-05-29 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200530_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(default='user', max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='123.456.7899', max_length=200),
        ),
    ]
