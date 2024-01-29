# Generated by Django 4.2.7 on 2024-01-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_profile_club_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='club_profile_status',
            field=models.CharField(blank=True, choices=[('No_club_member', 'No club member'), ('User_sent_join_request', 'User sent join request to Club'), ('Profile_change', 'Profile change'), ('Confirmed_profile', 'Confirmed profile'), ('Profile_rejected', 'Profile rejected')], default='No_club_member', max_length=100, null=True),
        ),
    ]