# Generated by Django 2.0.7 on 2018-07-29 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180729_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_item',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
