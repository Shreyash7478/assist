# Generated by Django 3.0 on 2019-12-15 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countries',
            name='language',
        ),
        migrations.CreateModel(
            name='LanguagesCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Countries')),
                ('languages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Languages')),
            ],
        ),
    ]
