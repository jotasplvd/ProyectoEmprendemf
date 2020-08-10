# Generated by Django 2.2.13 on 2020-08-07 22:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eficacia_global',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tramo', models.CharField(max_length=10)),
                ('porcentaje', models.DecimalField(decimal_places=2, max_digits=3)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]