# Generated by Django 3.1.5 on 2021-01-31 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=200)),
                ('Name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('name', models.CharField(max_length=40)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anbar.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order_status', models.CharField(choices=[('re', 'ready'), ('co', 'complete'), ('se', 'sent'), ('pe', 'pending')], max_length=10)),
                ('total_price', models.FloatField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anbar.customer')),
                ('product', models.ManyToManyField(to='anbar.Product')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anbar.employee'),
        ),
    ]