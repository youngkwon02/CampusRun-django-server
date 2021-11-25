# Generated by Django 3.2.7 on 2021-11-25 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_univ_domain'),
        ('game', '0006_invitation_is_read'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrance',
            fields=[
                ('ent_id', models.AutoField(primary_key=True, serialize=False)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ent_room', to='game.room')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ent_user', to='account.user')),
            ],
        ),
    ]
