# Generated by Django 4.1.7 on 2023-03-29 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100, unique=True)),
                ('born_date', models.CharField(max_length=50)),
                ('born_location', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=5000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes_app.author')),
                ('tags', models.ManyToManyField(to='quotes_app.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('done', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(to='quotes_app.tag')),
            ],
        ),
    ]
