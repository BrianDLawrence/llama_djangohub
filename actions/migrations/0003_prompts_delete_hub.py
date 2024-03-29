# Generated by Django 5.0.2 on 2024-02-15 14:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_hub'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prompts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1024)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prompts', to='actions.actions')),
            ],
        ),
        migrations.DeleteModel(
            name='HUB',
        ),
    ]
