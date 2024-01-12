# Generated by Django 5.0.1 on 2024-01-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_donor_idproof_alter_donor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='gender',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('accepted', 'accepted'), ('Assigned', 'Assigned'), ('pending', 'pending')], default='pending', max_length=200),
        ),
    ]