# Generated by Django 5.0 on 2024-01-10 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phosphodb_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expressionval',
            name='log2_fc',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='expressionval',
            name='p_value',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='expressionval',
            name='ratio',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
