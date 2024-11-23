# Generated by Django 4.2.16 on 2024-11-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('unique_sym', models.CharField(max_length=50)),
                ('sector', models.CharField(blank=True, max_length=200, null=True)),
                ('exchange', models.CharField(max_length=100)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]