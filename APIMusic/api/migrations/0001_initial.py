# Generated by Django 3.2.12 on 2022-06-25 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(max_length=15)),
                ('musical_genre', models.CharField(choices=[('ROCK', 'Rock'), ('INDIE_FOLK', 'Indie folk'), ('POP_ROCK', 'Pock rock'), ('ELECTRONIC', 'Electronic')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=15)),
                ('duration_in_minutes', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.band')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.album')),
            ],
        ),
        migrations.AddField(
            model_name='band',
            name='album',
            field=models.ManyToManyField(through='api.Song', to='api.Album'),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('middle_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('genre', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('role', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.band')),
            ],
        ),
    ]
