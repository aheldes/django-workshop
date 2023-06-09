# Generated by Django 4.2 on 2023-04-08 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('ocean_proximity_<1H OCEAN', '<1H OCEAN'), ('ocean_proximity_INLAND', 'INLAND'), ('ocean_proximity_ISLAND', 'ISLAND'), ('ocean_proximity_NEAR BAY', 'NEAR BAY'), ('ocean_proximity_NEAR OCEAN', 'NEAR OCEAN')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('housing_median_age', models.FloatField()),
                ('total_rooms', models.FloatField()),
                ('total_bedrooms', models.FloatField()),
                ('population', models.FloatField()),
                ('households', models.FloatField()),
                ('median_income', models.FloatField()),
                ('price', models.FloatField()),
                ('ocean_proximity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ml_app.location')),
            ],
        ),
    ]
