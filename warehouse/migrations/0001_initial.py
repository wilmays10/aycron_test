# Generated by Django 4.1.2 on 2022-11-16 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=30, verbose_name='Number')),
                ('street', models.CharField(blank=True, max_length=100, verbose_name='Address')),
                ('zipcode', models.CharField(blank=True, max_length=5, verbose_name='ZIP code')),
                ('state', models.CharField(blank=True, max_length=100, verbose_name='State')),
                ('county', models.CharField(blank=True, max_length=100, verbose_name='County')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField(unique=True, verbose_name='Code')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='warehouses', to='warehouse.address')),
            ],
        ),
    ]
