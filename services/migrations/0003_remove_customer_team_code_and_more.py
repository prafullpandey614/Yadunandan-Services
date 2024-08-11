# Generated by Django 5.0.7 on 2024-07-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_customer_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='team_code',
        ),
        migrations.AddField(
            model_name='customer',
            name='destination_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='source_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='state_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]