# Generated by Django 2.2.7 on 2019-12-04 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('diseases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Therapy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=100)),
                ('preparations', models.CharField(max_length=100)),
                ('treatment', models.CharField(max_length=100)),
                ('progress', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TherapyDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.TextField()),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diseases.Disease')),
                ('therapy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='therapy.Therapy')),
            ],
        ),
    ]
