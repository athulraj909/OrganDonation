# Generated by Django 5.0.1 on 2024-01-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='idproof',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donor',
            name='photo',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
