# Generated by Django 3.2.3 on 2021-06-07 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module_2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qna',
            name='answer',
            field=models.TextField(default='not answered yet'),
        ),
        migrations.AlterField(
            model_name='qna',
            name='doctor',
            field=models.CharField(default='not answered yet', max_length=69),
        ),
    ]