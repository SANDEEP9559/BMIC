# Generated by Django 4.0.3 on 2022-05-30 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr', models.IntegerField()),
                ('session', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr', models.IntegerField()),
                ('Class', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
