# Generated by Django 3.2.6 on 2022-03-14 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_clinicduration_specialty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinicduration',
            name='specialty',
        ),
    ]