# Generated by Django 4.2 on 2023-04-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11)),
                ('phone', models.CharField(max_length=15)),
                ('birthdate', models.DateField()),
            ],
        ),
    ]
