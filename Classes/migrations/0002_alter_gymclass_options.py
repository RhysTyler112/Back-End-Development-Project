# Generated by Django 4.2.17 on 2024-12-14 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gymclass',
            options={'ordering': ['date', 'time']},
        ),
    ]
