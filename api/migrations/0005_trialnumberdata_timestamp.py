# Generated by Django 3.1.2 on 2020-10-20 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201019_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='trialnumberdata',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
