# Generated by Django 5.0.2 on 2024-02-27 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookRadar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='ranking',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True),
        ),
    ]
