# Generated by Django 4.2.11 on 2024-03-13 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0008_context_alter_actions_name_delete_prompts'),
    ]

    operations = [
        migrations.AddField(
            model_name='actions',
            name='context',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='actions.context'),
        ),
    ]
