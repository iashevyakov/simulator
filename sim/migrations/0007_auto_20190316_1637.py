# Generated by Django 2.1.7 on 2019-03-16 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim', '0006_param_default_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
