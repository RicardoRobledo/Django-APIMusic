# Generated by Django 3.2.12 on 2022-08-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(max_length=15)),
                ('musical_genre', models.CharField(choices=[('ROCK', 'Rock'), ('INDIE_FOLK', 'Indie folk'), ('POP_ROCK', 'Pock rock'), ('ELECTRONIC', 'Electronic')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ManyToManyField(through='albums.Song', to='albums.Album')),
            ],
        ),
    ]
