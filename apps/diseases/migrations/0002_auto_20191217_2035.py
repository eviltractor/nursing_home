# Generated by Django 2.2.7 on 2019-12-17 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diseaseretired',
            old_name='discription',
            new_name='description',
        ),
    ]
