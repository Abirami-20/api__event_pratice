# Generated by Django 5.0 on 2024-03-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeEvents',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('participant_id', models.AutoField(primary_key=True, serialize=False)),
                ('participant_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('event_id', models.IntegerField()),
            ],
        ),
    ]
