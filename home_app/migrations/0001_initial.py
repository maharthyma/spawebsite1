# Generated by Django 3.2.2 on 2021-05-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('PhoneNumber', models.CharField(max_length=100)),
                ('Location', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Offer1', models.CharField(max_length=100)),
                ('Offer2', models.CharField(max_length=100)),
                ('Offer3', models.CharField(max_length=100)),
                ('Offer4', models.CharField(max_length=100)),
                ('Offer5', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Package',
            },
        ),
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('About', models.TextField()),
                ('Picture', models.FileField(upload_to='Portfolio')),
            ],
            options={
                'verbose_name_plural': 'Portfolio',
            },
        ),
    ]
