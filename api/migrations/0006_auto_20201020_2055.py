# Generated by Django 3.1.2 on 2020-10-20 20:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_trialnumberdata_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountdata',
            old_name='created_on',
            new_name='updated_time',
        ),
        migrations.RenameField(
            model_name='trialnumberdata',
            old_name='timestamp',
            new_name='created_time',
        ),
        migrations.AddField(
            model_name='accountdata',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alertdata',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alertdata',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='groupdata',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupdata',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='guestdata',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guestdata',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='accountdata',
            name='account_id',
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='accountdata',
            name='username',
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
    ]
