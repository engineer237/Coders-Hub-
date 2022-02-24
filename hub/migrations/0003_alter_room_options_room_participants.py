# Generated by Django 4.0.2 on 2022-02-24 11:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hub', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-date_created']},
        ),
        migrations.AddField(
            model_name='room',
            name='participants',
            field=models.ManyToManyField(related_name='Participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
