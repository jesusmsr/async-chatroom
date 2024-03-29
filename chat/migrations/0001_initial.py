# Generated by Django 4.1.7 on 2023-03-16 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_code', models.CharField(max_length=6, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('max_players', models.PositiveIntegerField(default=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
