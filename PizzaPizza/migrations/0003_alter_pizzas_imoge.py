# Generated by Django 5.0.4 on 2024-05-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0002_pizzas_imoge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzas',
            name='imoge',
            field=models.CharField(default='link', max_length=30),
            preserve_default=False,
        ),
    ]
