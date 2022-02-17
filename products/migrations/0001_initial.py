# Generated by Django 4.0.2 on 2022-02-17 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='PRODUCT', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.CharField(max_length=255)),
                ('featured', models.BooleanField()),
                ('nmbr_remaining', models.IntegerField(blank=True, null=True)),
                ('discontinued', models.BooleanField()),
                ('vegan', models.BooleanField()),
                ('gluten_free', models.BooleanField()),
                ('nut_free', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]