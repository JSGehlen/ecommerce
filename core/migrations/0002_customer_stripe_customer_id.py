# Generated by Django 3.0.6 on 2020-05-24 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='stripe_customer_id',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
