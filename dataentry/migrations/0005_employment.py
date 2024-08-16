# Generated by Django 5.1 on 2024-08-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0004_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employment_id', models.IntegerField()),
                ('employee_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=200)),
                ('salary', models.FloatField()),
                ('retirement', models.FloatField()),
                ('other_benefits', models.FloatField()),
                ('total_benefits', models.FloatField()),
                ('total_compensation', models.FloatField()),
            ],
        ),
    ]