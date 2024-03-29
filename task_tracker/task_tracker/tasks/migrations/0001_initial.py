# Generated by Django 5.0.1 on 2024-02-28 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('estimate', models.IntegerField()),
                ('state', models.CharField(choices=[('planned', 'Planned'), ('progress', 'Progress'), ('completed', 'Completed')], max_length=9)),
            ],
        ),
    ]
