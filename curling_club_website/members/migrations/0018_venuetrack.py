# Generated by Django 4.2.7 on 2024-02-24 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_venue_administrator'),
        ('members', '0017_alter_reservation_from_hour_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueTrack',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('note', models.CharField(blank=True, max_length=5, null=True)),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Resources_venue', to='events.venue')),
            ],
        ),
    ]