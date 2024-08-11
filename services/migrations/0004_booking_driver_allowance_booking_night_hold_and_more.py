# Generated by Django 5.0.7 on 2024-07-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_remove_customer_team_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='driver_allowance',
            field=models.FloatField(default=500),
        ),
        migrations.AddField(
            model_name='booking',
            name='night_hold',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='night_hold_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='sgst',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='cgst',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='igst',
            field=models.BooleanField(default=False),
        ),
    ]
