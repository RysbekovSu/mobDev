# Generated by Django 5.0.6 on 2024-06-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='price',
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='rate',
            field=models.IntegerField(db_index=True),
        ),
    ]
