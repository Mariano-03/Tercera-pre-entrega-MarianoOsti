# Generated by Django 5.1 on 2024-08-31 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liga_de_futbol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='jugador',
            name='fecha_nacimiento',
            field=models.DateField(),
        ),
    ]
