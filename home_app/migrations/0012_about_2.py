# Generated by Django 3.2.2 on 2021-05-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0011_auto_20210515_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('About_Heading', models.CharField(max_length=100)),
                ('About', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'About (for Home)',
            },
        ),
    ]
