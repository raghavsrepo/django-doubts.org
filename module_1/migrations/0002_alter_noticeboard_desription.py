# Generated by Django 3.2.3 on 2021-06-07 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticeboard',
            name='desription',
            field=models.TextField(default=''),
        ),
    ]
