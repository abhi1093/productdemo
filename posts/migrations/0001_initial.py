# Generated by Django 3.0.6 on 2020-08-20 06:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=40)),
                ('GST', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Cost', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Company')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('purchase_order_number', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Company')),
                ('product', models.ManyToManyField(to='posts.Product')),
            ],
        ),
    ]
