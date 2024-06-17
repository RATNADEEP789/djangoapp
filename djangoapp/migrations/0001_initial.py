# Generated by Django 5.0.6 on 2024-06-17 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registab',
            fields=[
                ('fld_slno', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(db_index=True, max_length=50, null=True)),
                ('dateofbirth', models.DateField(max_length=8)),
                ('gender', models.CharField(db_index=True, max_length=250)),
                ('mobile_number', models.CharField(db_index=True, max_length=100, null=True)),
                ('email_id', models.TextField(db_index=True, null=True)),
                ('home_town', models.CharField(db_index=True, max_length=250)),
                ('Username', models.CharField(db_index=True, max_length=250)),
                ('password', models.CharField(db_index=True, max_length=250)),
            ],
            options={
                'db_table': 'registab',
            },
        ),
    ]
