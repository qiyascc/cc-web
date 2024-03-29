# Generated by Django 5.0 on 2024-01-11 07:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='aboutText',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='github_link',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='instagram_link',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='linkedin_link',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='telegram_link',
        ),
        migrations.CreateModel(
            name='AboutText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutText', models.TextField()),
                ('userProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolioApp.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateRange', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technologies', models.JSONField()),
                ('userProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolioApp.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('imageUrl', models.URLField()),
                ('technologies', models.JSONField()),
                ('userProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolioApp.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.URLField()),
                ('instagram', models.URLField()),
                ('linkedin', models.URLField()),
                ('telegram', models.URLField()),
                ('userProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolioApp.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Writing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageUrl', models.URLField()),
                ('date', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('userProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolioApp.userprofile')),
            ],
        ),
    ]
