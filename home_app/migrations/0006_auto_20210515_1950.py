# Generated by Django 3.2.2 on 2021-05-15 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0005_auto_20210515_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='About_Picture',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='Picture',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='review',
            name='Image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='service',
            name='Image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='team',
            name='Picture',
            field=models.FileField(upload_to=''),
        ),
    ]