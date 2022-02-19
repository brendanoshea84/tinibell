# Generated by Django 4.0.2 on 2022-02-19 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('label', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=255)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
    ]
