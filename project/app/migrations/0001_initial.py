# Generated by Django 4.2.4 on 2023-09-01 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=100)),
                ('ucontact', models.CharField(max_length=20)),
                ('uemail', models.EmailField(max_length=254)),
            ],
        ),
    ]
