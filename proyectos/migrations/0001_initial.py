# Generated by Django 2.2.3 on 2021-01-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField(max_length=500)),
                ('codigo_fuente', models.URLField()),
                ('url', models.URLField()),
            ],
        ),
    ]
