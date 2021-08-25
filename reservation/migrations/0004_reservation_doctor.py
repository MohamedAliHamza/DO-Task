# Generated by Django 3.2.6 on 2021-08-24 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0003_alter_reservation_clinic'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_reservation', to='user.user'),
            preserve_default=False,
        ),
    ]
