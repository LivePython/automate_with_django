# Generated by Django 5.1 on 2024-08-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_num', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
