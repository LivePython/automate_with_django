# Generated by Django 5.1 on 2024-09-08 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0005_emailtracking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sent', models.IntegerField()),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emails.email')),
            ],
        ),
    ]
