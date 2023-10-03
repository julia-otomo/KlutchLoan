# Generated by Django 4.2.5 on 2023-10-03 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('phone', models.CharField(max_length=12, unique=True)),
            ],
        ),
    ]
