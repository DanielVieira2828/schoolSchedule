# Generated by Django 5.0.6 on 2024-10-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('ra', models.CharField(default='', max_length=20, unique=True)),
                ('max_horas', models.FloatField()),
                ('horas_atuais', models.FloatField(default=0.0)),
            ],
        ),
    ]
