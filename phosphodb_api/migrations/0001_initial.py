# Generated by Django 5.0 on 2024-01-03 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CellOrTissue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_type', models.CharField(choices=[('cell', 'cell'), ('tissue', 'tissue')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='CellTypeDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='ExpCondition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('utf8_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Pmid',
            fields=[
                ('pmid', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]