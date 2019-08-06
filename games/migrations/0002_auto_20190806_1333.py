# Generated by Django 2.2.1 on 2019-08-06 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EsbrRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('description',),
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=2)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='game',
            name='esrb_rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='games.EsbrRating'),
        ),
        migrations.CreateModel(
            name='PlayerScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('score_date', models.DateTimeField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='games.Player')),
            ],
            options={
                'ordering': ('-score',),
            },
        ),
    ]
