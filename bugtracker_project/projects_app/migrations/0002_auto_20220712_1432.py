# Generated by Django 3.0.8 on 2022-07-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='bug_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='team_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
