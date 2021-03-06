# Generated by Django 3.0.8 on 2020-07-11 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_payment_payment_intent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='primary_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_products', to='cart.Category'),
        ),
    ]
