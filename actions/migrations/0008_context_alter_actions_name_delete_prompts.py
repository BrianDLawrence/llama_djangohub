# Generated by Django 4.2.11 on 2024-03-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0007_actions_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='actions',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.DeleteModel(
            name='Prompts',
        ),
    ]