# Generated by Django 5.0.4 on 2024-05-02 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzas',
            name='imoge',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
